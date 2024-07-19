from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import HDD, SSD, PSU, GPU, GroupNomenklatyra, Motherboard, Product, Ram, Processor, Manufacturer, \
    DriveType, FormFactorHDD, HDDInterface, PSUPurpose, GPUFormFactor, GPUFamily
from .forms import HDDForm, SSDForm, PSUForm, GPUForm, GroupNomenklatyraForm, MotherboardForm, ProductForm, RamForm, \
    ProcessorForm, ManufacturerForm, DriveTypeForm, FormFactorHDDForm, HDDInterfaceForm, PSUPurposeForm, \
    GPUFormFactorForm, GPUFamilyForm


class ProductListView(ListView):
    model = Product
    template_name = 'nomenklatyra/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'nomenklatyra/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'nomenklatyra/product_form.html'
    success_url = reverse_lazy('product_list')

# HDD views
class HDDListView(ListView):
    model = HDD
    template_name = 'nomenklatyra/hdd_list.html'
    context_object_name = 'hdds'

class HDDCreateView(CreateView):
    model = HDD
    form_class = HDDForm
    template_name = 'nomenklatyra/hdd_form.html'
    success_url = reverse_lazy('hdd_list')

class HDDUpdateView(UpdateView):
    model = HDD
    form_class = HDDForm
    template_name = 'nomenklatyra/hdd_form.html'
    success_url = reverse_lazy('hdd_list')

# SSD views
class SSDListView(ListView):
    model = SSD
    template_name = 'nomenklatyra/ssd_list.html'
    context_object_name = 'ssds'

class SSDCreateView(CreateView):
    model = SSD
    form_class = SSDForm
    template_name = 'nomenklatyra/ssd_form.html'
    success_url = reverse_lazy('ssd_list')

class SSDUpdateView(UpdateView):
    model = SSD
    form_class = SSDForm
    template_name = 'nomenklatyra/ssd_form.html'
    success_url = reverse_lazy('ssd_list')

# PSU views
class PSUListView(ListView):
    model = PSU
    template_name = 'nomenklatyra/psu_list.html'
    context_object_name = 'psus'

class PSUCreateView(CreateView):
    model = PSU
    form_class = PSUForm
    template_name = 'nomenklatyra/psu_form.html'
    success_url = reverse_lazy('psu_list')

class PSUUpdateView(UpdateView):
    model = PSU
    form_class = PSUForm
    template_name = 'nomenklatyra/psu_form.html'
    success_url = reverse_lazy('psu_list')

# GPU views
class GPUListView(ListView):
    model = GPU
    template_name = 'nomenklatyra/gpu_list.html'
    context_object_name = 'gpus'

class GPUCreateView(CreateView):
    model = GPU
    form_class = GPUForm
    template_name = 'nomenklatyra/gpu_form.html'
    success_url = reverse_lazy('gpu_list')

class GPUUpdateView(UpdateView):
    model = GPU
    form_class = GPUForm
    template_name = 'nomenklatyra/gpu_form.html'
    success_url = reverse_lazy('gpu_list')

# GroupNomenklatyra views
class GroupNomenklatyraListView(ListView):
    model = GroupNomenklatyra
    template_name = 'nomenklatyra/groupnomenklatyra_list.html'
    context_object_name = 'groupnomenklatyras'

class GroupNomenklatyraCreateView(CreateView):
    model = GroupNomenklatyra
    form_class = GroupNomenklatyraForm
    template_name = 'nomenklatyra/groupnomenklatyra_form.html'
    success_url = reverse_lazy('groupnomenklatyra_list')

class GroupNomenklatyraUpdateView(UpdateView):
    model = GroupNomenklatyra
    form_class = GroupNomenklatyraForm
    template_name = 'nomenklatyra/groupnomenklatyra_form.html'
    success_url = reverse_lazy('groupnomenklatyra_list')

# Motherboard views
class MotherboardListView(ListView):
    model = Motherboard
    template_name = 'nomenklatyra/motherboard_list.html'
    context_object_name = 'motherboards'

class MotherboardCreateView(CreateView):
    model = Motherboard
    form_class = MotherboardForm
    template_name = 'nomenklatyra/motherboard_form.html'
    success_url = reverse_lazy('motherboard_list')

class MotherboardUpdateView(UpdateView):
    model = Motherboard
    form_class = MotherboardForm
    template_name = 'nomenklatyra/motherboard_form.html'
    success_url = reverse_lazy('motherboard_list')

# Ram views
class RamListView(ListView):
    model = Ram
    template_name = 'nomenklatyra/ram_list.html'
    context_object_name = 'rams'

class RamCreateView(CreateView):
    model = Ram
    form_class = RamForm
    template_name = 'nomenklatyra/ram_form.html'
    success_url = reverse_lazy('ram_list')

class RamUpdateView(UpdateView):
    model = Ram
    form_class = RamForm
    template_name = 'nomenklatyra/ram_form.html'
    success_url = reverse_lazy('ram_list')

# Processor views
class ProcessorListView(ListView):
    model = Processor
    template_name = 'nomenklatyra/processor_list.html'
    context_object_name = 'processors'

class ProcessorCreateView(CreateView):
    model = Processor
    form_class = ProcessorForm
    template_name = 'nomenklatyra/processor_form.html'
    success_url = reverse_lazy('processor_list')

class ProcessorUpdateView(UpdateView):
    model = Processor
    form_class = ProcessorForm
    template_name = 'nomenklatyra/processor_form.html'
    success_url = reverse_lazy('processor_list')

class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'nomenklatyra/manufacturer_list.html'
    context_object_name = 'manufacturers'

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'nomenklatyra/manufacturer_form.html'
    success_url = reverse_lazy('manufacturer_list')

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'nomenklatyra/manufacturer_form.html'
    success_url = reverse_lazy('manufacturer_list')



class DriveTypeListView(ListView):
    model = DriveType
    template_name = 'nomenklatyra/drivetype_list.html'
    context_object_name = 'drivetypes'

class DriveTypeCreateView(CreateView):
    model = DriveType
    form_class = DriveTypeForm
    template_name = 'nomenklatyra/drivetype_form.html'
    success_url = reverse_lazy('drivetype_list')

class DriveTypeUpdateView(UpdateView):
    model = DriveType
    form_class = DriveTypeForm
    template_name = 'nomenklatyra/drivetype_form.html'
    success_url = reverse_lazy('drivetype_list')


class FormFactorHDDListView(ListView):
    model = FormFactorHDD
    template_name = 'nomenklatyra/formfactorhdd_list.html'
    context_object_name = 'formfactors'

class FormFactorHDDCreateView(CreateView):
    model = FormFactorHDD
    form_class = FormFactorHDDForm
    template_name = 'nomenklatyra/formfactorhdd_form.html'
    success_url = reverse_lazy('formfactorhdd_list')

class FormFactorHDDUpdateView(UpdateView):
    model = FormFactorHDD
    form_class = FormFactorHDDForm
    template_name = 'nomenklatyra/formfactorhdd_form.html'
    success_url = reverse_lazy('formfactorhdd_list')



class HDDInterfaceListView(ListView):
    model = HDDInterface
    template_name = 'nomenklatyra/hddinterface_list.html'
    context_object_name = 'interfaces'

class HDDInterfaceCreateView(CreateView):
    model = HDDInterface
    form_class = HDDInterfaceForm
    template_name = 'nomenklatyra/hddinterface_form.html'
    success_url = reverse_lazy('hddinterface_list')

class HDDInterfaceUpdateView(UpdateView):
    model = HDDInterface
    form_class = HDDInterfaceForm
    template_name = 'nomenklatyra/hddinterface_form.html'
    success_url = reverse_lazy('hddinterface_list')


class SSDCreateView(CreateView):
    model = SSD
    form_class = SSDForm
    template_name = 'nomenklatyra/ssd_form.html'
    success_url = reverse_lazy('ssd_list')

class SSDUpdateView(UpdateView):
    model = SSD
    form_class = SSDForm
    template_name = 'nomenklatyra/ssd_form.html'
    success_url = reverse_lazy('ssd_list')


class PSUPurposeListView(ListView):
    model = PSUPurpose
    template_name = 'nomenklatyra/psupurpose_list.html'
    context_object_name = 'psupurposes'

class PSUPurposeCreateView(CreateView):
    model = PSUPurpose
    form_class = PSUPurposeForm
    template_name = 'nomenklatyra/psupurpose_form.html'
    success_url = reverse_lazy('psupurpose_list')

class PSUPurposeUpdateView(UpdateView):
    model = PSUPurpose
    form_class = PSUPurposeForm
    template_name = 'nomenklatyra/psupurpose_form.html'
    success_url = reverse_lazy('psupurpose_list')


class GPUFormFactorListView(ListView):
    model = GPUFormFactor
    template_name = 'nomenklatyra/gpuformfactor_list.html'
    context_object_name = 'gpu_formfactors'

class GPUFormFactorCreateView(CreateView):
    model = GPUFormFactor
    form_class = GPUFormFactorForm
    template_name = 'nomenklatyra/gpuformfactor_form.html'
    success_url = reverse_lazy('gpu_formfactor_list')

class GPUFormFactorUpdateView(UpdateView):
    model = GPUFormFactor
    form_class = GPUFormFactorForm
    template_name = 'nomenklatyra/gpuformfactor_form.html'
    success_url = reverse_lazy('gpu_formfactor_list')


class GPUFamilyListView(ListView):
    model = GPUFamily
    template_name = 'nomenklatyra/gpufamily_list.html'
    context_object_name = 'gpufamilies'

class GPUFamilyCreateView(CreateView):
    model = GPUFamily
    form_class = GPUFamilyForm
    template_name = 'nomenklatyra/gpufamily_form.html'
    success_url = reverse_lazy('gpufamily_list')

class GPUFamilyUpdateView(UpdateView):
    model = GPUFamily
    form_class = GPUFamilyForm
    template_name = 'nomenklatyra/gpufamily_form.html'
    success_url = reverse_lazy('gpufamily_list')