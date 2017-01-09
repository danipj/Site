# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-09 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Arquivo', max_length=100)),
                ('Arquivo', models.FileField(upload_to='web/')),
                ('tipo', models.CharField(choices=[('BannerAtivo', 'BannerAtivo'), ('BanneInativo', 'BanneInativo'), ('ImagensGeral', 'ImagensGeral'), ('Outros', 'Outros')], default='Outros', max_length=30)),
                ('descricao', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
