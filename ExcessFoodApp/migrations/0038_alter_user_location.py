# Generated by Django 3.2.23 on 2024-02-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0037_alter_food_prepared_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.IntegerField(null=True),
        ),
    ]
