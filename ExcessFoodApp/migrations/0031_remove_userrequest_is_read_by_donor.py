# Generated by Django 3.2.23 on 2023-12-28 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0030_userrequest_seen_donor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequest',
            name='is_read_by_donor',
        ),
    ]
