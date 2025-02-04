# Generated by Django 4.2.18 on 2025-02-04 16:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название места')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Координаты')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('region', models.CharField(blank=True, max_length=100, verbose_name='Регион')),
                ('postal_code', models.CharField(blank=True, max_length=10, verbose_name='Почтовый индекс')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
                'ordering': ['city', 'name'],
            },
        ),
    ]
