# Generated by Django 3.1.3 on 2020-12-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaBadaniaWadWzroku', '0013_auto_20201201_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='information1',
            name='disease_pl',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='information1',
            name='disease_ru',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
