from django import forms
from .models import HDD, SSD, PSU, GPU, GroupNomenklatyra, Motherboard, Product, Ram, Processor, Manufacturer, \
    DriveType, FormFactorHDD, HDDInterface, PSUPurpose, GPUFormFactor, GPUFamily


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class HDDForm(forms.ModelForm):
    class Meta:
        model = HDD
        fields = '__all__'
        labels = {
            'name': 'Назва номенклатури',
            'group': 'Група',
            'manufacturer': 'Виробник',
            'drive_type': 'Тип накопичувача',
            'capacity': 'Обсяг пам\'яті',
            'form_factor': 'Форм-фактор HDD',
            'interface': 'Інтерфейс підключення HDD',
        }
        widgets = {
            'drive_type': forms.Select(attrs={'class': 'form-control'}),
        }
class SSDForm(forms.ModelForm):
    class Meta:
        model = SSD
        fields = '__all__'


class GPUForm(forms.ModelForm):
    class Meta:
        model = GPU
        fields = ['name', 'group', 'manufacturer', 'family', 'form_factor', 'intended_use', 'chip', 'interface', 'memory_capacity', 'memory_type', 'connectors']
class GroupNomenklatyraForm(forms.ModelForm):
    class Meta:
        model = GroupNomenklatyra
        fields = '__all__'

class MotherboardForm(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'

class RamForm(forms.ModelForm):
    class Meta:
        model = Ram
        fields = '__all__'

class ProcessorForm(forms.ModelForm):
    class Meta:
        model = Processor
        fields = '__all__'

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'



class DriveTypeForm(forms.ModelForm):
    class Meta:
        model = DriveType
        fields = '__all__'
        labels = {
            'name': 'Тип накопичувача',
        }


class FormFactorHDDForm(forms.ModelForm):
    class Meta:
        model = FormFactorHDD
        fields = '__all__'

class HDDForm(forms.ModelForm):
    class Meta:
        model = HDD
        fields = '__all__'


class HDDInterfaceForm(forms.ModelForm):
    class Meta:
        model = HDDInterface
        fields = '__all__'

class HDDForm(forms.ModelForm):
    class Meta:
        model = HDD
        fields = '__all__'

class SSDForm(forms.ModelForm):
    class Meta:
        model = SSD
        fields = '__all__'


class PSUPurposeForm(forms.ModelForm):
    class Meta:
        model = PSUPurpose
        fields = '__all__'

class PSUForm(forms.ModelForm):
    class Meta:
        model = PSU
        fields = '__all__'


class GPUFormFactorForm(forms.ModelForm):
    class Meta:
        model = GPUFormFactor
        fields = ['name']

class GPUFamilyForm(forms.ModelForm):
    class Meta:
        model = GPUFamily
        fields = ['name']