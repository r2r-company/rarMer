# Generated by Django 5.0.6 on 2024-07-12 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва компанії')),
                ('address', models.CharField(max_length=255, verbose_name='Адреса')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Компанія',
                'verbose_name_plural': 'Компанії',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва підрозділу')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='companies.company', verbose_name='Компанія')),
            ],
            options={
                'verbose_name': 'Підрозділ',
                'verbose_name_plural': 'Підрозділи',
            },
        ),
    ]
