# Generated by Django 5.0 on 2025-04-08 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kushalapp', '0009_remove_lead_current_followup_remove_lead_lead_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_visited', models.BooleanField()),
                ('inspection_done', models.BooleanField()),
                ('lead_type', models.CharField(choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold'), ('Not Interested', 'Not Interested')], max_length=20)),
                ('quotation_given', models.BooleanField()),
                ('quotation_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quotation_file', models.FileField(blank=True, null=True, upload_to='quotations/')),
                ('second_followup_date', models.DateField()),
                ('lead', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kushalapp.lead')),
                ('second_followup_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_followup_person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
