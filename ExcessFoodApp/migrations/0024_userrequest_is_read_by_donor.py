# Generated by Django 3.2.23 on 2023-12-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0023_userrequest_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='is_read_by_donor',
            field=models.BooleanField(default=False),
        ),
    ]
