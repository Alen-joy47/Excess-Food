# Generated by Django 3.2.23 on 2024-02-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0035_auto_20240219_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='location',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
