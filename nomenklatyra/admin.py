from django.contrib import admin
from .models import GroupNomenklatyra, Product, Processor, Motherboard, Ram, SSD, GPU, HDD, PSU

@admin.register(GroupNomenklatyra)
class GroupNomenklatyraAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer']

@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'family', 'socket', 'cores', 'threads', 'base_clock', 'integrated_graphics']

@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'intended_use', 'socket', 'chipset_model', 'ram_type', 'onboard_video', 'raid_controller', 'form_factor']

@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'intended_use', 'capacity', 'type', 'frequency']

@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'drive_type', 'capacity', 'form_factor', 'interface']

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'family', 'form_factor', 'intended_use', 'chip', 'interface', 'memory_capacity', 'memory_type', 'connectors']

@admin.register(HDD)
class HDDAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'drive_type', 'capacity', 'form_factor', 'interface']

@admin.register(PSU)
class PSUAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'manufacturer', 'intended_use']
