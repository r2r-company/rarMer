from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EquipmentReceipt, EquipmentTransfer, EquipmentInventory, EquipmentWriteOff

@receiver(post_save, sender=EquipmentReceipt)
def create_inventory_on_receipt(sender, instance, created, **kwargs):
    if created:
        EquipmentInventory.objects.create(
            item=instance.item,
            company=instance.company,
            department=instance.department,
            employee=instance.employee,
            status='Прихід товару'
        )

@receiver(post_save, sender=EquipmentTransfer)
def update_inventory_on_transfer(sender, instance, **kwargs):
    try:
        inventory = EquipmentInventory.objects.get(id=instance.inventory.id)
        inventory.department = instance.to_department
        inventory.employee = instance.to_employee
        inventory.status = 'Переміщений товар'
        inventory.save()
    except EquipmentInventory.DoesNotExist:
        pass

@receiver(post_save, sender=EquipmentWriteOff)
def update_inventory_on_writeoff(sender, instance, **kwargs):
    inventory = instance.inventory
    inventory.status = 'Списаний товар'
    inventory.save()
