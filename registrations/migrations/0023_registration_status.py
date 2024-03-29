# Generated by Django 3.2.16 on 2023-05-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0022_auto_20230502_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('draft', 'models:registration:status_draft'), ('submitted', 'models:registration:status_submitted'), ('registered', 'models:registration:status_registered')], default='draft', max_length=20),
        ),
    ]
