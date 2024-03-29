# Generated by Django 4.2.3 on 2023-08-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0027_rename_description_attachment_file_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('faqs', models.ManyToManyField(to='registrations.faq')),
            ],
        ),
    ]
