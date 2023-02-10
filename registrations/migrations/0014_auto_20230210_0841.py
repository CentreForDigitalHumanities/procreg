# Generated by Django 3.2.16 on 2023-02-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0013_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('upload', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('not_approved', models.PositiveIntegerField(blank=True, choices=[('yes', 'models:choices:yes'), ('no', 'models:choices:no'), ('', 'models:choices:please_specify')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='follows_policy',
            field=models.CharField(choices=[('yes', 'models:choices:yes'), ('no', 'models:choices:no'), ('', 'models:choices:please_specify')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='registration',
            name='policy_additions',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='registration',
            name='policy_exceptions',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
    ]