# Generated by Django 3.2.16 on 2023-05-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0021_auto_20230418_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='involves_guardian_consent',
            new_name='involves_guardian',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='involves_consent',
            new_name='involves_knowingly',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='involves_non_consent',
            new_name='involves_not_knowingly',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='involves_other_people',
            new_name='involves_other',
        ),
        migrations.AlterField(
            model_name='involved',
            name='group_type',
            field=models.CharField(choices=[('knowingly', 'models:involved:knowingly'), ('not_knowingly', 'models:involved:not_knowingly'), ('guardian', 'models:involved:guardian'), ('other', 'models:involved:other')], max_length=25),
        ),
    ]
