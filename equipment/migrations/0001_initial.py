# Generated by Django 5.0.6 on 2024-07-12 20:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('nomenklatyra', '0001_initial'),
        ('userprofile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_use', 'Використовується'), ('in_storage', 'На складі'), ('under_maintenance', 'На обслуговуванні')], default='in_storage', max_length=255, verbose_name='Статус')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Компанія')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.department', verbose_name='Підрозділ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Працівник')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenklatyra.product', verbose_name='Номенклатура')),
            ],
            options={
                'verbose_name': 'Запас обладнання',
                'verbose_name_plural': 'Запаси обладнання',
            },
        ),
        migrations.CreateModel(
            name='EquipmentReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Кількість')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата приходу')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Компанія')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.department', verbose_name='Підрозділ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.userprofile', verbose_name='Працівник')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenklatyra.product', verbose_name='Номенклатура')),
            ],
            options={
                'verbose_name': 'Прихід обладнання',
                'verbose_name_plural': 'Приходи обладнання',
            },
        ),
        migrations.CreateModel(
            name='EquipmentTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата переміщення')),
                ('from_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_from', to='companies.company', verbose_name='З компанії')),
                ('from_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfer_from', to='companies.department', verbose_name='З підрозділу')),
                ('from_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfer_from', to='userprofile.userprofile', verbose_name='Від працівника')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenklatyra.product', verbose_name='Номенклатура')),
                ('to_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_to', to='companies.company', verbose_name='До компанії')),
                ('to_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfer_to', to='companies.department', verbose_name='До підрозділу')),
                ('to_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfer_to', to='userprofile.userprofile', verbose_name='До працівника')),
            ],
            options={
                'verbose_name': 'Переміщення обладнання',
                'verbose_name_plural': 'Переміщення обладнання',
            },
        ),
        migrations.CreateModel(
            name='EquipmentWriteOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(verbose_name='Причина списання')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата списання')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='Компанія')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.department', verbose_name='Підрозділ')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.userprofile', verbose_name='Працівник')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenklatyra.product', verbose_name='Номенклатура')),
            ],
            options={
                'verbose_name': 'Списання обладнання',
                'verbose_name_plural': 'Списання обладнання',
            },
        ),
    ]
