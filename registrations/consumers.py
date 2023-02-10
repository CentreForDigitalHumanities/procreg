from cdh.questions.blueprints import BaseConsumer, BaseQuestionConsumer

from .forms import NewRegistrationQuestion, FacultyQuestion, \
    UsesInformationQuestion, InvolvedPeopleQuestion, NewInvolvedQuestion, \
    PurposeQuestion, RetentionQuestion, ConfirmInformationUseQuestion, \
    TraversalQuestion, GoalQuestion, ReceiverQuestion, NewReceiverQuestion
from .models import Involved, Receiver


class RegistrationConsumer(BaseQuestionConsumer):

    def get_question_data(self):
        question_data = super().get_question_data()
        question_data["registration"] = self.blueprint.object
        return question_data

    def add_error(self, *args):
        return self.blueprint.errors.add(*args)

    def add_question_error(self, *args):
        try:
            slug = self.question.slug
        except AttributeError as e:
            raise e("Question or slug undefined")
        return self.blueprint.errors.add(slug, *args)


class TopQuestionsConsumer(BaseConsumer):

    def consume(self):
        "If both top questions are filled out, append the next consumer"
        # Fetch the instantiated top questions from blueprint
        new_reg, fac = (
            self.blueprint.get_question(q.slug) for q in
            [NewRegistrationQuestion, FacultyQuestion]
        )
        # Set them to incomplete if they have errors
        self.blueprint.top_questions_incomplete = False
        for q in (new_reg, fac):
            q.complete = True
            if len(self.blueprint.errors[q.slug]) != 0:
                q.incomplete = True
                self.blueprint.top_questions_incomplete = True
        self.enable_summary()
        return [TraversalConsumer]

    def enable_summary(self):
        from .views import RegistrationSummaryView
        view = RegistrationSummaryView(
            reg_pk=self.blueprint.object.pk,
        )
        self.blueprint.questions.append(view)


class NewRegistrationConsumer(RegistrationConsumer):

    question_class = NewRegistrationQuestion

    def consume(self):
        self.blueprint.top_questions.append(
            self.question,
        )
        self.get_errors()
        self.blueprint.completed.append(self.question)
        # TopQuestionsConsumer checks for our errors, so we can just return
        return []

    def get_errors(self):
        self.errors = self.get_django_errors()
        for f in self.empty_fields:
            self.errors.append(f"Field {f} is empty")
        for field, error in self.errors.items():
            self.blueprint.errors.add(self.question.slug, field, error)


class FacultyConsumer(RegistrationConsumer):

    question_class = FacultyQuestion

    def consume(self):
        self.blueprint.top_questions.append(
            self.question,
        )
        self.get_errors()
        self.blueprint.completed.append(self.question)
        # TopQuestionsConsumer checks for our errors, so we can just return
        return []

    def get_errors(self):
        self.errors = self.get_django_errors()
        for f, v in self.errors.items():
            self.blueprint.errors.add(
                self.question.slug, f, v,
            )
        for f in self.empty_fields:
            self.blueprint.errors.add(
                self.question.slug,
                f,
                f"Field {f} is empty",
            )


class TraversalConsumer(BaseQuestionConsumer):

    question_class = TraversalQuestion

    def consume(self):
        self.blueprint.questions.append(
            self.question,
        )
        return [GoalConsumer]


class GoalConsumer(BaseQuestionConsumer):

    question_class = GoalQuestion

    def consume(self):
        self.blueprint.questions.append(
            self.question,
        )
        return [InvolvedPeopleConsumer]


class InvolvedPeopleConsumer(BaseQuestionConsumer):

    question_class = InvolvedPeopleQuestion

    def consume(self):
        """For each involved group, add the relevant consumer."""
        registration = self.blueprint.object
        self.blueprint.desired_next.append(self.question)
        self.blueprint.questions.append(self.question)
        # Check if one required groups are checked
        if True not in [
                registration.involves_consent,
                registration.involves_non_consent,
        ]:
            return self.no_group_selected()
        self.question.complete = True
        # Fetch relevant consumer and manager for user selection
        consumers, managers = self._get_selected()
        # Finally, return
        if consumers != []:
            return [GroupManagerConsumer] + consumers + [RetentionConsumer]
        else:
            return []

    def no_group_selected(self):
        self.question.incomplete = True
        return []

    def _get_selected(self):
        """Return the appropriate lists of consumers and managers for the
        booleans set on the registration"""
        registration = self.blueprint.object
        selected = []
        managers = []
        consumer_dict = {
            'involves_consent':
            (ConsentGroupConsumer, "consent"),
            'involves_non_consent':
            (NonConsentGroupConsumer, "non_consent"),
            'involves_guardian_consent':
            (GuardianGroupConsumer, "guardian_consent"),
            'involves_other_people':
            (OtherGroupConsumer, "other"),
        }
        for group in self.question.Meta.fields:
            if getattr(registration, group) is True:
                consumer, group_type = consumer_dict[group]
                # These consumers will be added to this function's output
                selected.append(consumer)
                # These managers should show up in the progress bar
                managers.append(self._construct_manager_view(group_type))
        return selected, managers

    def _construct_manager_view(self, group_type):
        # Importing here to prevent circular import
        from .views import InvolvedManager
        return InvolvedManager(
            registration=self.blueprint.object,
        )


class GroupManagerConsumer(BaseConsumer):
    """This consumer is added when at least one group of a type
    is needed, and succeeds if at least one group of each type
    has been added."""
    success_list = []

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_manager(self):
        from .views import InvolvedManager
        return InvolvedManager(
            registration=self.blueprint.object,
        )

    def consume(self):
        self.manager = self.get_manager()
        self.blueprint.questions.append(self.manager)
        return []


class ConsentManagerConsumer(GroupManagerConsumer):

    group_type = "consent"


class BaseGroupConsumer(BaseQuestionConsumer):

    question_class = NewInvolvedQuestion
    group_type = None
    success_list = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add our group type to the blueprint for the
        # InvolvedManager can easily find which ones are selected
        if self.group_type:
            self.blueprint.selected_groups.append(
                self.group_type,
            )

    @property
    def group_qs(self):
        registration = self.blueprint.object
        return Involved.objects.filter(
            registration=registration,
            group_type=self.group_type,
        )

    def instantiate(self):
        """Add a question with empty Involved for new group creation"""
        self.question = self.question_class(
            instance=Involved(
                group_type=self.group_type,
            ),
            blueprint=self.blueprint,
            registration=self.blueprint.object,
        )
        return self.question

    def consume(self):
        # First add the empty question to blueprint
        # This will allow the user to create new groups
        if self.question.instance.group_type is None:
            breakpoint()
        self.blueprint.questions.append(self.question)
        # Then search for existing groups to manage
        for group in self.group_qs:
            # Instantiate the question with instance
            iq = self.question_class(
                instance=group,
                blueprint=self.blueprint,
            )
            self.blueprint.questions.append(iq)
        if self.has_entries():
            if self.check_details():
                return self.success()
        return self.fail()

    def check_details(self):
        return True

    def has_entries(self):
        return not len(self.group_qs) == 0

    def success(self):
        return self.success_list

    def fail(self):
        return []


class ConsentGroupConsumer(BaseGroupConsumer):

    group_type = "consent"


class NonConsentGroupConsumer(BaseGroupConsumer):

    group_type = "non_consent"


class GuardianGroupConsumer(BaseGroupConsumer):

    group_type = "guardian_consent"


class OtherGroupConsumer(BaseGroupConsumer):

    group_type = "other"


class PurposeConsumer(BaseQuestionConsumer):

    question = PurposeQuestion


class RetentionConsumer(RegistrationConsumer):

    question_class = RetentionQuestion

    def consume(self):

        self.blueprint.questions.append(self.question)
        
        return [ReceiverConsumer]


class ReceiverConsumer(RegistrationConsumer):

    question_class = ReceiverQuestion

    def consume(self):
        registration = self.blueprint.object
        self.blueprint.questions.append(self.question)
        if self.blueprint.object.third_party_sharing == "yes":
            return [NewReceiverConsumer]
        elif self.blueprint.object.third_party_sharing == "no":
            return [SoftwareManagerConsumer]
        else:
            return []


class NewReceiverConsumer(BaseConsumer):
    """This consumer instantiates a question for each Receiver
    connected to the registration. Additionally it instantiates
    an empty one for the addition of a new Receiver."""

    question_class = ReceiverQuestion

    def consume(self):
        self.registration = self.blueprint.object
        self.instantiate_all()
        if self.at_least_one_created():
            if self.no_errors():
                return [SoftwareManagerConsumer]
        return []

    def at_least_one_created(self):
        return self.get_queryset().count() > 0

    def no_errors(self):
        return True

    def instantiate_all(self):
        """Populate self.questions with all Receivers plus one
        empty one"""
        self.questions = []
        for receiver in self.get_queryset():
            self.questions.append(
                NewReceiverQuestion(
                    blueprint=self.blueprint,
                    instance=receiver,
                )
            )
        self.questions.append(
            NewReceiverQuestion(
                blueprint=self.blueprint,
                # NOTE: This one is intentionally empty
                instance=Receiver(),
            )
        )
        self.blueprint.questions += self.questions

    def get_queryset(self):
        return Receiver.objects.filter(
            registration=self.blueprint.object,
        )

    def none_added(self):
        self.blueprint.errors.add(
            ReceiverQuestion.slug,
        )
        return []


class SoftwareManagerConsumer(BaseConsumer):

    def consume(self):
        return []


class ConfirmInformationUseConsumer(BaseQuestionConsumer):

    question_class = ConfirmInformationUseQuestion

    def consume(self):
        self.blueprint.desired_next.append(self.question)
        return []