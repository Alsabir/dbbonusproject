# Generated by Django 3.2.9 on 2021-11-17 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0004_alter_disease_pathogen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='discover',
            options={'ordering': ['-first_enc_date'], 'verbose_name_plural': 'Discoveries'},
        ),
        migrations.AlterModelOptions(
            name='specialize',
            options={'verbose_name_plural': 'Specializaions'},
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.publicservant'),
        ),
    ]
