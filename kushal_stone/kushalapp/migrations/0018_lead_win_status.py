# Generated by Django 5.0 on 2025-04-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kushalapp', '0017_alter_followup3_next_followup_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='win_status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
