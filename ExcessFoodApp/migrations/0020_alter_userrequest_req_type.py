# Generated by Django 3.2.23 on 2023-12-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0019_rename_request_userrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='req_type',
            field=models.IntegerField(default=1),
        ),
    ]
