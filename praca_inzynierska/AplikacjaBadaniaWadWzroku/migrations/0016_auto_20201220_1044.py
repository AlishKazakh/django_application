# Generated by Django 3.1.3 on 2020-12-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaBadaniaWadWzroku', '0015_information1_disease_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information1',
            name='disease_pl',
        ),
        migrations.RemoveField(
            model_name='information1',
            name='disease_ru',
        ),
        migrations.AddField(
            model_name='information1',
            name='disease_name_pl',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='information1',
            name='disease_name_ru',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]