# Generated by Django 5.0.1 on 2025-02-04 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_car_fuel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='leads',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='leads',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='orders',
        ),
    ]
