# Generated by Django 5.0 on 2025-04-08 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kushalapp', '0011_rename_second_followup_date_followup1_followup_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='follow_up_date',
            new_name='followup_date',
        ),
    ]
