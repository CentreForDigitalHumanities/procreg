# Generated by Django 3.2.16 on 2023-01-31 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0012_auto_20230131_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('outside_eer', models.CharField(choices=[('yes', 'models:choices:yes'), ('no', 'models:choices:no'), ('', 'models:choices:please_specify')], max_length=10)),
                ('basis_for_transfer', models.CharField(choices=[('explicit_permission', 'models:receiver:explicit_permission'), ('adequacy_decision', 'models:receiver:adequacy_decision'), ('standard_contractual', 'models:receiver:standard_contractual'), ('other', 'models:receiver:other'), ('no_basis', 'models:receiver:no_basis'), ('', 'models:choices:please_specify')], default='', max_length=200)),
                ('explanation', models.TextField(default='', max_length=2000)),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='registrations.registration')),
            ],
        ),
    ]