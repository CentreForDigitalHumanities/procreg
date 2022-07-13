# Generated by Django 3.2.12 on 2022-06-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_registration_uses_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='confirm_submission',
            field=models.BooleanField(choices=[(False, 'models:registration:confirm_submission_false'), (True, 'models:registration:confirm_submission_true')], default=False),
        ),
    ]