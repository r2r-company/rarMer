# Generated by Django 5.0.6 on 2024-07-19 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapravka', '0002_cartridge_delete_zapravka_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='number',
            field=models.IntegerField(verbose_name='№ картриджа'),
        ),
    ]
