# Generated by Django 3.2.23 on 2024-02-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0039_auto_20240222_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
