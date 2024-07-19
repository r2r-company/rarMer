from django.db import models
from django.contrib.auth.models import User
from companies.models import Company, Department

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Компанія')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Підрозділ')
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.user.username