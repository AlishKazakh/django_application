# Generated by Django 3.1.3 on 2020-12-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaBadaniaWadWzroku', '0014_auto_20201220_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='information1',
            name='disease_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]