# Generated by Django 5.0.1 on 2025-01-27 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_lead_is_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='flat_number',
            new_name='map_link',
        ),
    ]
