# Generated by Django 5.0.1 on 2025-02-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_lead_ca_comments_lead_cce_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
