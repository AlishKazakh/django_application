# Generated by Django 3.1.3 on 2020-12-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaBadaniaWadWzroku', '0010_auto_20201201_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_information', models.TextField(default='')),
                ('disease_symptoms', models.TextField(default='')),
                ('disease_treatment', models.TextField(default='')),
                ('disease', models.CharField(default='', max_length=50)),
                ('language', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
