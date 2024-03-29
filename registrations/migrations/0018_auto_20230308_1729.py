# Generated by Django 3.2.16 on 2023-03-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0017_alter_software_not_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ICFormDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegularDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SensitiveDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecialDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='InformationKind',
        ),
        migrations.AddField(
            model_name='involved',
            name='algemeen_belang_details',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='involved',
            name='confirm_parental_permission',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='explicit_permission_details',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='involved',
            name='gave_explicit_permission',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='government_supervised_collection',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='grounds_for_exception',
            field=models.CharField(choices=[('public', 'models:involved:public_grounds'), ('algemeen_belang', 'models:involved:algemeen_belang'), ('legal', 'models:involved:legal_grounds')], default='', max_length=25),
        ),
        migrations.AddField(
            model_name='involved',
            name='involves_children_under_15',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='legal_grounds_details',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='involved',
            name='provides_criminal_information',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='provides_ic_form',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='provides_no_sensitive_details',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='involved',
            name='extra_details',
            field=models.ManyToManyField(to='registrations.ExtraDetail'),
        ),
        migrations.AddField(
            model_name='involved',
            name='ic_form_details',
            field=models.ManyToManyField(to='registrations.ICFormDetail'),
        ),
        migrations.AddField(
            model_name='involved',
            name='other_sensitive_details',
            field=models.ManyToManyField(to='registrations.SensitiveDetail'),
        ),
        migrations.AddField(
            model_name='involved',
            name='regular_details',
            field=models.ManyToManyField(to='registrations.RegularDetail'),
        ),
        migrations.AddField(
            model_name='involved',
            name='social_media_details',
            field=models.ManyToManyField(to='registrations.SocialMediaDetail'),
        ),
        migrations.AddField(
            model_name='involved',
            name='special_details',
            field=models.ManyToManyField(to='registrations.SpecialDetail'),
        ),
    ]
