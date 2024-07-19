from django.db import models
from django.contrib.auth.models import User

class ComputerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавьте это поле
    hostname = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=45)
    memory_info = models.TextField()
    motherboard_info = models.TextField()
    processor_info = models.TextField()
    storage_info = models.TextField()
    free_space_c = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.hostname

class ComputerChanges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=15)
    disk_space = models.FloatField()
    changes = models.TextField()
    timestamp = models.DateTimeField()

class ChangeLog(models.Model):
    computer = models.ForeignKey(ComputerInfo, on_delete=models.CASCADE)
    changed_fields = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Changes for {self.computer.hostname} at {self.timestamp}"