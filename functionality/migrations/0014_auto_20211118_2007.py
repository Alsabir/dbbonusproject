# Generated by Django 3.2.9 on 2021-11-18 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0013_auto_20211118_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='cname',
            field=models.ForeignKey(db_column='cname', on_delete=django.db.models.deletion.CASCADE, to='functionality.country'),
        ),
        migrations.AlterField(
            model_name='record',
            name='disease_code',
            field=models.ForeignKey(db_column='disease_code', on_delete=django.db.models.deletion.CASCADE, to='functionality.disease'),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='functionality.publicservant'),
        ),
    ]
