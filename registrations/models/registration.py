from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

# Create your models here.

USER_MODEL = get_user_model()

YES_NO = (
    ('yes', "models:choices:yes"),
    ('no', "models:choices:no"),
    ('', "models:choices:please_specify"),
)
YES_NO_NA = (
    ('yes', "models:choices:yes"),
    ('no', "models:choices:no"),
    ('n_a', "models:choices:non_applicable"),
    ('', "models:choices:please_specify"),
)

class Registration(models.Model):

    # Meta information
    registration_title = models.CharField(
        max_length=200,
        help_text=_("models:registration_title_help_text"),
        verbose_name=_("models:registrations:title_verbose_name"),
    )
    created_by = models.ForeignKey(USER_MODEL,
                                   on_delete=models.SET_DEFAULT,
                                   related_name="registrations_created",
                                   blank=True,
                                   null=True,
                                   default=None,
                                   )
    created_on = models.DateTimeField(auto_now=True)
    STATUSES = (
        ("draft", "models:registration:status_draft"),
        ("submitted", "models:registration:status_submitted"),
        ("registered", "models:registration:status_registered"),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default="draft",
    )

    # Blueprint information
    applicants = models.ManyToManyField(USER_MODEL,
                                        related_name="applicant_for",
                                        blank=True,
                                        )
    faculty = models.CharField(max_length=100,
                               blank=True,
                               default=None,
                               null=True,
                               )
    uses_information = models.BooleanField(
        blank=True,
        null=True,
        choices=(
            (False, _("models:registration:registration_uses_information_false")),
            (True, _("models:registration:registration_uses_information_true")),
             )
        )
    date_start = models.DateField(blank=True,
                                  null=True,
                                  )
    date_end = models.DateField(blank=True,
                                null=True,
                                )
    research_goal = models.TextField(
        default="",
        max_length=500,
    )
    confirm_submission = models.BooleanField(
        default=False,
        choices=(
            (False, _("models:registration:confirm_submission_false")),
            (True, _("models:registration:confirm_submission_true")),
             )
        )

    involves_knowingly = models.BooleanField(
        default=False,
    )
    involves_not_knowingly = models.BooleanField(
        default=False,
    )
    involves_guardian = models.BooleanField(
        default=False,
    )
    involves_other = models.BooleanField(
        default=False,
    )

    # Retention question
    raw_storage_location = models.CharField(
        max_length=250,
        default="",
        blank=True,
    )
    raw_data_decade = models.CharField(
        max_length=10,
        choices=YES_NO,
        default="",
    )
    ic_storage_location = models.CharField(
        max_length=250,
        default="",
        blank=True,
    )
    ic_storage_decade = models.CharField(
        max_length=10,
        choices=YES_NO,
        default="",
    )
    audio_video_kept = models.CharField(
        max_length=10,
        choices=YES_NO_NA,
        default="",
    )
    audio_video_kept_details = models.CharField(
        max_length=250,
        default="",
        blank=True,
    )

    
    # Storage question
    # These are charfields for future-proofing and consistency
   
    data_storage = models.CharField(
        max_length=25,
        choices=YES_NO,
        default="",
    )
    consent_document_storage = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        default="",
    )
    multimedia_storage = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        default="",
    )

    # Third parties

    third_party_sharing = models.CharField(
        max_length=25,
        choices=YES_NO,
        default="",
    )

    # Software question

    uses_software = models.CharField(
        max_length=10,
        choices=YES_NO,
        default="",
    )

    # Security questions

    follows_policy = models.CharField(
        max_length=10,
        choices=YES_NO,
        default="",
    )
    policy_exceptions = models.TextField(
        max_length=2000,
        default="",
        blank=True,
    )
    policy_additions = models.TextField(
        max_length=2000,
        default="",
        blank=True,
    )

    # Misc

    submitter_comments = models.TextField(
        max_length = 1000,
        default = "",
        blank=True,
    )

    def list_involved_types(self):
        """
        Return a list of involved group types involved in this registration.
        Group types are given in Involved.GROUP_TYPES style.
        """
        group_dict = {
            'involves_knowingly': "knowingly",
            'involves_not_knowingly': "not_knowingly",
            'involves_guardian': "guardian",
            'involves_other': "other",
        }
        involved = filter(
            lambda key: getattr(self, key),
            group_dict.keys(),
        )
        return [group_dict[t] for t in involved]
