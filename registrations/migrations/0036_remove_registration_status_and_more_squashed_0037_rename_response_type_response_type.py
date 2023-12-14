# Generated by Django 4.2.6 on 2023-12-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('registrations', '0036_remove_registration_status_and_more'), ('registrations', '0037_rename_response_type_response_type')]

    dependencies = [
        ('registrations', '0035_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='status',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='submitter_comments',
        ),
        migrations.RemoveField(
            model_name='response',
            name='approved',
        ),
        migrations.AddField(
            model_name='response',
            name='status',
            field=models.CharField(choices=[('draft', 'models:response:status_draft'), ('submitted', 'models:response:status_submitted'), ('registered', 'models:response:status_registered')], default='draft', help_text='models:response:status_help_text', max_length=20, verbose_name='models:response:status_verbose_name'),
        ),
        migrations.AlterField(
            model_name='response',
            name='comments',
            field=models.CharField(blank=True, default='', help_text='models:response:comments_help_text', max_length=1000, verbose_name='models:response:comments_verbose_name'),
        ),
        migrations.AddField(
            model_name='response',
            name='type',
            field=models.CharField(blank=True, choices=[('PO', 'PO Response'), ('USER', 'User Response')], default='', max_length=20),
        ),
    ]
