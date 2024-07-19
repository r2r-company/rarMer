from django import template
from collections import defaultdict

register = template.Library()

@register.filter
def group_by_department(queryset):
    grouped = defaultdict(list)
    for item in queryset:
        department = item.department.name if item.department else 'Без підрозділу'
        grouped[department].append(item)
    return grouped.items()
