# Generated by Django 4.2.3 on 2023-07-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0025_faq_question_slugs_faq_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='title',
            new_name='registration_title',
        ),
    ]