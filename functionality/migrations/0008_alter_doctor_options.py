# Generated by Django 3.2.9 on 2021-11-17 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0007_auto_20211118_0436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'permissions': [('doctor_access', 'doctor_access')]},
        ),
    ]