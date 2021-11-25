# Generated by Django 3.2.9 on 2021-11-15 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Email', max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='First Name', max_length=30)),
                ('surname', models.CharField(help_text='Surname', max_length=40)),
                ('salary', models.PositiveIntegerField(help_text='Annual salary')),
                ('phone', models.CharField(help_text='Phone number', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(help_text='Description of the disease type', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='functionality.myuser')),
                ('degree', models.CharField(help_text='Degree', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='functionality.myuser')),
                ('department', models.CharField(help_text='Department', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(help_text='Disease code', max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(help_text='Pathogen', max_length=20)),
                ('description', models.CharField(help_text='Description of the disease', max_length=140)),
                ('id_DiseaseType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.diseasetype')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='cname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.country'),
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_enc_date', models.DateField(verbose_name='First encounter date')),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.disease')),
            ],
            options={
                'ordering': ['-first_enc_date'],
                'unique_together': {('disease_code', 'cname')},
            },
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_DiseaseType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.diseasetype')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.doctor')),
            ],
            options={
                'unique_together': {('email', 'id_DiseaseType')},
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_death', models.PositiveIntegerField(help_text='Total deaths')),
                ('total_patients', models.PositiveIntegerField(help_text='Total patients treated')),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.disease')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functionality.doctor')),
            ],
            options={
                'unique_together': {('email', 'disease_code', 'cname')},
            },
        ),
    ]
