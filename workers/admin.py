from django.contrib import admin
from equipment.models import EquipmentReceipt, EquipmentTransfer

from .models import Worker

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'hire_date']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'position']


