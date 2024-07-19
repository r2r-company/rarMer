from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, HDDListView, HDDCreateView, HDDUpdateView, \
    SSDListView, SSDCreateView, SSDUpdateView, PSUListView, PSUCreateView, PSUUpdateView, GPUListView, GPUCreateView, \
    GPUUpdateView, GroupNomenklatyraListView, GroupNomenklatyraCreateView, GroupNomenklatyraUpdateView, \
    MotherboardListView, MotherboardCreateView, MotherboardUpdateView, RamListView, RamCreateView, RamUpdateView, \
    ProcessorListView, ProcessorCreateView, ProcessorUpdateView, ManufacturerListView, ManufacturerCreateView, \
    ManufacturerUpdateView, DriveTypeListView, DriveTypeCreateView, DriveTypeUpdateView, FormFactorHDDListView, \
    FormFactorHDDCreateView, FormFactorHDDUpdateView, HDDInterfaceListView, HDDInterfaceCreateView, \
    HDDInterfaceUpdateView, PSUPurposeListView, PSUPurposeCreateView, PSUPurposeUpdateView, GPUFormFactorListView, \
    GPUFormFactorCreateView, GPUFormFactorUpdateView, GPUFamilyListView, GPUFamilyCreateView, GPUFamilyUpdateView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

    path('hdds/', HDDListView.as_view(), name='hdd_list'),
    path('hdds/add/', HDDCreateView.as_view(), name='hdd_create'),
    path('hdds/edit/<int:pk>/', HDDUpdateView.as_view(), name='hdd_update'),

    path('ssds/', SSDListView.as_view(), name='ssd_list'),
    path('ssds/add/', SSDCreateView.as_view(), name='ssd_create'),
    path('ssds/edit/<int:pk>/', SSDUpdateView.as_view(), name='ssd_update'),

    path('psus/', PSUListView.as_view(), name='psu_list'),
    path('psus/add/', PSUCreateView.as_view(), name='psu_create'),
    path('psus/edit/<int:pk>/', PSUUpdateView.as_view(), name='psu_update'),

    path('gpus/', GPUListView.as_view(), name='gpu_list'),
    path('gpus/add/', GPUCreateView.as_view(), name='gpu_create'),
    path('gpus/edit/<int:pk>/', GPUUpdateView.as_view(), name='gpu_update'),

    path('groupnomenklatyras/', GroupNomenklatyraListView.as_view(), name='groupnomenklatyra_list'),
    path('groupnomenklatyras/add/', GroupNomenklatyraCreateView.as_view(), name='groupnomenklatyra_create'),
    path('groupnomenklatyras/edit/<int:pk>/', GroupNomenklatyraUpdateView.as_view(), name='groupnomenklatyra_update'),

    path('motherboards/', MotherboardListView.as_view(), name='motherboard_list'),
    path('motherboards/add/', MotherboardCreateView.as_view(), name='motherboard_create'),
    path('motherboards/edit/<int:pk>/', MotherboardUpdateView.as_view(), name='motherboard_update'),

    path('rams/', RamListView.as_view(), name='ram_list'),
    path('rams/add/', RamCreateView.as_view(), name='ram_create'),
    path('rams/edit/<int:pk>/', RamUpdateView.as_view(), name='ram_update'),

    path('processors/', ProcessorListView.as_view(), name='processor_list'),
    path('processors/add/', ProcessorCreateView.as_view(), name='processor_create'),
    path('processors/edit/<int:pk>/', ProcessorUpdateView.as_view(), name='processor_update'),

    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturers/add/', ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturers/edit/<int:pk>/', ManufacturerUpdateView.as_view(), name='manufacturer_update'),

    path('drivetypes/', DriveTypeListView.as_view(), name='drivetype_list'),
    path('drivetypes/add/', DriveTypeCreateView.as_view(), name='drivetype_create'),
    path('drivetypes/edit/<int:pk>/', DriveTypeUpdateView.as_view(), name='drivetype_update'),

    path('formfactors/', FormFactorHDDListView.as_view(), name='formfactorhdd_list'),
    path('formfactors/add/', FormFactorHDDCreateView.as_view(), name='formfactorhdd_create'),
    path('formfactors/edit/<int:pk>/', FormFactorHDDUpdateView.as_view(), name='formfactorhdd_update'),

    path('hddinterfaces/', HDDInterfaceListView.as_view(), name='hddinterface_list'),
    path('hddinterfaces/add/', HDDInterfaceCreateView.as_view(), name='hddinterface_create'),
    path('hddinterfaces/edit/<int:pk>/', HDDInterfaceUpdateView.as_view(), name='hddinterface_update'),

    path('ssds/', SSDListView.as_view(), name='ssd_list'),
    path('ssds/add/', SSDCreateView.as_view(), name='ssd_create'),
    path('ssds/edit/<int:pk>/', SSDUpdateView.as_view(), name='ssd_update'),

    path('psupurposes/', PSUPurposeListView.as_view(), name='psupurpose_list'),
    path('psupurposes/add/', PSUPurposeCreateView.as_view(), name='psupurpose_create'),
    path('psupurposes/edit/<int:pk>/', PSUPurposeUpdateView.as_view(), name='psupurpose_update'),

    path('gpu_formfactors/', GPUFormFactorListView.as_view(), name='gpu_formfactor_list'),
    path('gpu_formfactors/add/', GPUFormFactorCreateView.as_view(), name='gpu_formfactor_create'),
    path('gpu_formfactors/edit/<int:pk>/', GPUFormFactorUpdateView.as_view(), name='gpu_formfactor_update'),

    path('gpufamilies/', GPUFamilyListView.as_view(), name='gpufamily_list'),
    path('gpufamilies/add/', GPUFamilyCreateView.as_view(), name='gpufamily_create'),
    path('gpufamilies/edit/<int:pk>/', GPUFamilyUpdateView.as_view(), name='gpufamily_update'),
]
