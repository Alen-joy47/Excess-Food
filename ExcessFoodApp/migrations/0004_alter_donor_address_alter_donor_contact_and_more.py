# Generated by Django 4.2.7 on 2023-12-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0003_donor_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='password',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
