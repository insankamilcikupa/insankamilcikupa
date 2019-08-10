# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaftarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('tempat_lahir', models.CharField(max_length=20)),
                ('jenis_kelamin', models.CharField(max_length=5)),
                ('alamat', models.CharField(max_length=50)),
                ('nama_ayah', models.CharField(max_length=50)),
                ('pekerjaan_ortu', models.CharField(max_length=20)),
                ('pendidikan_ortu', models.CharField(max_length=15)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]