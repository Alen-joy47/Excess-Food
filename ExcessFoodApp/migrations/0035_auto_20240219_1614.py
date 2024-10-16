# Generated by Django 3.2.23 on 2024-02-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0034_alter_userrequest_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('values', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'places',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
