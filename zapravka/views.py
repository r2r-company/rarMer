from companies.models import Department
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from workers.models import Worker
from zapravka.utils import send_telegram_message

from .models import Cartridge
from .forms import CartridgeForm
from django.http import JsonResponse
from django.db.models import Prefetch

def add_cartridge(request):
    if request.method == 'POST':
        form = CartridgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartridge_list')
    else:
        form = CartridgeForm()
    return render(request, 'zapravka/add_cartridge.html', {'form': form})


def cartridge_list(request):
    filled_cartridges = Cartridge.objects.filter(status='Заправлений')
    empty_cartridges = Cartridge.objects.filter(status='Порожній')
    return render(request, 'zapravka/cartridge_list.html', {'filled_cartridges': filled_cartridges, 'empty_cartridges': empty_cartridges})

def update_cartridge_status(request, cartridge_id):
    cartridge = get_object_or_404(Cartridge, id=cartridge_id)
    cartridge.status = 'Порожній' if cartridge.status == 'Заправлений' else 'Заправлений'
    cartridge.save()
    return JsonResponse({'status': 'success'})

@csrf_exempt
def change_cartridge_status(request):
    if request.method == 'POST':
        cartridge_id = request.POST.get('id')
        new_status = request.POST.get('status')
        try:
            cartridge = Cartridge.objects.get(id=cartridge_id)
            cartridge.status = 'Порожній' if new_status == 'empty' else 'Заправлений'
            cartridge.save()

            # Формування повідомлення для Telegram
            message = f"Назва картриджа: {cartridge.name} №{cartridge.number} - Статус: {cartridge.status}\n"
            departments = Department.objects.all().prefetch_related(Prefetch('cartridge_set', queryset=Cartridge.objects.all()))
            for department in departments:
                cartridges = department.cartridge_set.all()
                if cartridges:
                    message += f"{department.name}\n"
                    for i, cartridge in enumerate(cartridges, 1):
                        message += f"{i}. {cartridge.name} №{cartridge.number} - {cartridge.status}\n"
                    message += "\n"

            send_telegram_message(message)

            return JsonResponse({'success': True})
        except Cartridge.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Картридж не знайдено'})
    return JsonResponse({'success': False, 'error': 'Некоректний запит'})


def get_departments(request):
    company_id = request.GET.get('company_id')
    departments = Department.objects.filter(company_id=company_id).order_by('name')
    workers = Worker.objects.filter(company_id=company_id).order_by('user__last_name')
    return JsonResponse({
        'departments': list(departments.values('id', 'name')),
        'workers': list(workers.values('id', 'user__first_name', 'user__last_name'))
    })

def get_workers(request):
    department_id = request.GET.get('department_id')
    workers = Worker.objects.filter(department_id=department_id).order_by('user__last_name')
    return JsonResponse({
        'workers': list(workers.values('id', 'user__first_name', 'user__last_name'))
    })


@csrf_exempt
def change_status_from_telegram(request, cartridge_id):
    try:
        cartridge = Cartridge.objects.get(id=cartridge_id)
        cartridge.status = 'Заправлений'
        cartridge.save()
        return JsonResponse({'success': True})
    except Cartridge.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Картридж не знайдено'})


def list_cartridges(request):
    cartridges = Cartridge.objects.filter(status='Порожній')
    if not cartridges.exists():
        return JsonResponse({'message': 'Всі картриджі заправлені'})

    data = [{'id': cartridge.id, 'name': cartridge.name, 'number': cartridge.number, 'status': cartridge.status} for
            cartridge in cartridges]
    return JsonResponse(data, safe=False)