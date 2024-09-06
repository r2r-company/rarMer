from django.contrib import admin
from .models import Site, TariffPlan, Payment

# Реєстрація моделей в адмінці
admin.site.register(Site)
admin.site.register(TariffPlan)
admin.site.register(Payment)
