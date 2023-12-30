# Generated by Django 3.2.23 on 2023-12-28 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExcessFoodApp', '0025_donor_un_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrequest',
            old_name='is_read_by_donor',
            new_name='is_read',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='un_read',
        ),
        migrations.AddField(
            model_name='userrequest',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='ExcessFoodApp.donor'),
        ),
    ]
