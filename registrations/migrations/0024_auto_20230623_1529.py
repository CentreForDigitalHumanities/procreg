# Generated by Django 3.2.16 on 2023-06-23 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0023_registration_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('upload', models.FileField(upload_to='')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='registrations.registration')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
