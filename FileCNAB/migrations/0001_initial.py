# Generated by Django 4.1.5 on 2023-02-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileCNAB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(max_length=1)),
                ('data', models.TextField(max_length=8)),
                ('valor', models.IntegerField(max_length=10)),
                ('CPF', models.IntegerField(max_length=11)),
                ('cartão', models.IntegerField(max_length=12)),
                ('hora', models.IntegerField(max_length=6)),
                ('dono', models.TextField(max_length=14)),
                ('loja', models.TextField(max_length=19)),
            ],
        ),
    ]
