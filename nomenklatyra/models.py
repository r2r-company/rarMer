from django.db import models



class GroupNomenklatyra(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва групи')

    class Meta:
        verbose_name = 'Група номенклатури'
        verbose_name_plural = 'Групи номенкла   тури'

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва виробника')

    class Meta:
        verbose_name = 'Виробник'
        verbose_name_plural = 'Виробники'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва номенклатури')
    group = models.ForeignKey(GroupNomenklatyra, on_delete=models.CASCADE, related_name='products', verbose_name='Група')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Виробник')

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'

    def __str__(self):
        return self.name

class Processor(Product):
    family = models.CharField(max_length=255, blank=True, null=True, verbose_name='Сімейство процесора')
    socket = models.CharField(max_length=255, blank=True, null=True, verbose_name='Сокет')
    cores = models.IntegerField(blank=True, null=True, verbose_name='Кількість ядер')
    threads = models.IntegerField(blank=True, null=True, verbose_name='Кількість потоків')
    base_clock = models.CharField(max_length=255, blank=True, null=True, verbose_name='Базова тактова частота процесора')
    integrated_graphics = models.CharField(max_length=255, blank=True, null=True, verbose_name='Графічне ядро')

    class Meta:
        verbose_name = 'Процесор'
        verbose_name_plural = 'Процесори'

class Motherboard(Product):
    intended_use = models.CharField(max_length=255, blank=True, null=True, verbose_name='Призначення материнської плати')
    socket = models.CharField(max_length=255, blank=True, null=True, verbose_name='Сокет')
    chipset_model = models.CharField(max_length=255, blank=True, null=True, verbose_name='Модель чіпсета')
    ram_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип ОЗУ')
    onboard_video = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вбудоване відео')
    raid_controller = models.CharField(max_length=255, blank=True, null=True, verbose_name='Контролер RAID')
    form_factor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Форма-фактор материнської плати')

    class Meta:
        verbose_name = 'Материнська плата'
        verbose_name_plural = 'Материнські плати'

class Ram(Product):
    intended_use = models.CharField(max_length=255, blank=True, null=True, verbose_name='Призначення оперативної пам\'яті')
    capacity = models.CharField(max_length=255, blank=True, null=True, verbose_name='Обсяг пам\'яті')
    type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип пам\'яті')
    frequency = models.CharField(max_length=255, blank=True, null=True, verbose_name='Частота пам\'яті')

    class Meta:
        verbose_name = 'Оперативна пам\'ять'
        verbose_name_plural = 'Оперативні пам\'яті'


class GPUFamily(models.Model):
    name = models.CharField(max_length=255, verbose_name='Сімейство графіки')

    class Meta:
        verbose_name = 'Сімейство графіки'
        verbose_name_plural = 'Сімейства графіки'

    def __str__(self):
        return self.name

class GPUFormFactor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Форм-фактор відеокарти')

    class Meta:
        verbose_name = 'Форм-фактор відеокарти'
        verbose_name_plural = 'Форм-фактори відеокарт'

    def __str__(self):
        return self.name

class GPU(Product):
    family = models.ForeignKey(GPUFamily, on_delete=models.CASCADE, verbose_name='Сімейство графіки')
    form_factor = models.ForeignKey(GPUFormFactor, on_delete=models.CASCADE, verbose_name='Форм-фактор відеокарти')
    intended_use = models.CharField(max_length=255, blank=True, null=True, verbose_name='Призначення відеокарти')
    chip = models.CharField(max_length=255, blank=True, null=True, verbose_name='Графічний чіп')
    interface = models.CharField(max_length=255, blank=True, null=True, verbose_name='Інтерфейс підключення відеокарти')
    memory_capacity = models.CharField(max_length=255, blank=True, null=True, verbose_name='Обсяг пам\'яті відеокарти')
    memory_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип пам\'яті відеокарти')
    connectors = models.CharField(max_length=255, blank=True, null=True, verbose_name='Роз\'єми відеокарти')

    class Meta:
        verbose_name = 'Відеокарта'
        verbose_name_plural = 'Відеокарти'

class DriveType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип накопичувача')

    class Meta:
        verbose_name = 'Тип накопичувача'
        verbose_name_plural = 'Типи накопичувачів'

    def __str__(self):
        return self.name

class FormFactorHDD(models.Model):
    name = models.CharField(max_length=255, verbose_name='Форм-фактор HDD')

    class Meta:
        verbose_name = 'Форм-фактор HDD'
        verbose_name_plural = 'Форм-фактори HDD'

    def __str__(self):
        return self.name

class HDDInterface(models.Model):
    name = models.CharField(max_length=255, verbose_name='Інтерфейс підключення HDD')

    class Meta:
        verbose_name = 'Інтерфейс підключення HDD'
        verbose_name_plural = 'Інтерфейси підключення HDD'

    def __str__(self):
        return self.name

class HDD(Product):
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE, verbose_name='Тип накопичувача')
    capacity = models.CharField(max_length=255, blank=True, null=True, verbose_name='Обсяг пам\'яті')
    form_factor = models.ForeignKey(FormFactorHDD, on_delete=models.CASCADE, verbose_name='Форм-фактор HDD')
    interface = models.ForeignKey(HDDInterface, on_delete=models.CASCADE, verbose_name='Інтерфейс підключення HDD')

    class Meta:
        verbose_name = 'HDD'
        verbose_name_plural = 'HDD-диски'


class SSD(Product):
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE, verbose_name='Тип накопичувача')
    capacity = models.CharField(max_length=255, blank=True, null=True, verbose_name='Обсяг пам\'яті')
    form_factor = models.ForeignKey(FormFactorHDD, on_delete=models.CASCADE, verbose_name='Форм-фактор SSD')
    interface = models.ForeignKey(HDDInterface, on_delete=models.CASCADE, verbose_name='Інтерфейс підключення SSD')

    class Meta:
        verbose_name = 'SSD'
        verbose_name_plural = 'SSD-диски'

class PSUPurpose(models.Model):
    name = models.CharField(max_length=255, verbose_name='Призначення блока живлення')

    class Meta:
        verbose_name = 'Призначення блока живлення'
        verbose_name_plural = 'Призначення блоків живлення'

    def __str__(self):
        return self.name

class PSU(Product):
    intended_use = models.ForeignKey(PSUPurpose, on_delete=models.CASCADE, verbose_name='Призначення блока живлення')

    class Meta:
        verbose_name = 'Блок живлення'
        verbose_name_plural = 'Блоки живлення'




