# Generated by Django 3.2.23 on 2023-12-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0015_food_quantity_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_deliverable',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='prepared_time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
