# Generated by Django 4.1.5 on 2023-02-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileCNAB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecnab',
            name='CPF',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filecnab',
            name='cartão',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filecnab',
            name='hora',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filecnab',
            name='tipo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filecnab',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
