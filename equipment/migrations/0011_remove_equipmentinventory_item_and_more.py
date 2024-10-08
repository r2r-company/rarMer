# Generated by Django 5.0.6 on 2024-07-15 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('equipment', '0010_equipmentinventory_employee'),
        ('nomenklatyra', '0001_initial'),
        ('workers', '0002_worker_company_worker_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentinventory',
            name='item',
        ),
        migrations.RemoveField(
            model_name='equipmenttransfer',
            name='receipt',
        ),
        migrations.RemoveField(
            model_name='equipmenttransfer',
            name='to_company',
        ),
        migrations.RemoveField(
            model_name='equipmentwriteoff',
            name='company',
        ),
        migrations.RemoveField(
            model_name='equipmentwriteoff',
            name='department',
        ),
        migrations.RemoveField(
            model_name='equipmentwriteoff',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='equipmentwriteoff',
            name='item',
        ),
        migrations.AddField(
            model_name='equipmentinventory',
            name='receipt',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='equipment.equipmentreceipt', verbose_name='Прихід'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipmenttransfer',
            name='inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipment.equipmentinventory', verbose_name='Запас'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipmentwriteoff',
            name='inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipment.equipmentinventory', verbose_name='Запас'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipmentreceipt',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Компанія'),
        ),
        migrations.AlterField(
            model_name='equipmentreceipt',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата приходу'),
        ),
        migrations.AlterField(
            model_name='equipmentreceipt',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.department', verbose_name='Підрозділ'),
        ),
        migrations.AlterField(
            model_name='equipmentreceipt',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.worker', verbose_name='Працівник'),
        ),
        migrations.AlterField(
            model_name='equipmentreceipt',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenklatyra.product', verbose_name='Номенклатура'),
        ),
        migrations.AlterField(
            model_name='equipmenttransfer',
            name='to_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.department', verbose_name='Новий підрозділ'),
        ),
        migrations.AlterField(
            model_name='equipmenttransfer',
            name='to_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.worker', verbose_name='Новий працівник'),
        ),
    ]
