# Generated by Django 4.2.3 on 2023-10-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0032_faqlist_show_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='submitter_comments',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
