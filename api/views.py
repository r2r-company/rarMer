from companies.models import Company, Department
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import ComputerInfo, ChangeLog
from zapravka.models import Cartridge


def dashboard(request):
    companies = Company.objects.all()
    return render(request, 'api/dashboard.html', {'companies': companies})

def api_departments(request):
    company_id = request.GET.get('company_id')
    departments = Department.objects.filter(company_id=company_id)
    data = [{'id': dept.id, 'name': dept.name} for dept in departments]
    return JsonResponse(data, safe=False)

def api_users(request):
    company_id = request.GET.get('company_id')
    department_id = request.GET.get('department_id')

    if company_id and department_id:
        users = User.objects.filter(userprofile__company_id=company_id, userprofile__department_id=department_id)
    elif company_id:
        users = User.objects.filter(userprofile__company_id=company_id)
    else:
        users = User.objects.all()

    data = [{'id': user.id, 'username': user.username} for user in users]
    return JsonResponse(data, safe=False)

def api_computer_info(request):
    user_id = request.GET.get('user_id')
    computer_info = ComputerInfo.objects.filter(user_id=user_id).first()
    if computer_info:
        data = {
            'hostname': computer_info.hostname,
            'ip_address': computer_info.ip_address,
            'disk_space': computer_info.disk_space
        }
    else:
        data = {}
    return JsonResponse(data)

@csrf_exempt
def live_data(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        computer_info = ComputerInfo.objects.filter(user_id=user_id).first()
        if computer_info:
            data = {
                'hostname': computer_info.hostname,
                'ip_address': computer_info.ip_address,
                'free_space_c': computer_info.free_space_c
            }
        else:
            data = {}
        print("Sending live data:", data)  # Отладочный вывод
        return JsonResponse(data)
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def notify(request):
    try:
        data = json.loads(request.body)
        hostname = data.get("hostname")
        ip_address = data.get("ip_address")
        memory_info = data.get("memory_info")
        motherboard_info = data.get("motherboard_info")
        processor_info = data.get("processor_info")
        storage_info = data.get("storage_info")
        free_space_c = data.get("free_space_c")
        user_id = data.get("user_id")

        user = User.objects.get(id=user_id)

        ComputerInfo.objects.create(
            hostname=hostname,
            ip_address=ip_address,
            memory_info=memory_info,
            motherboard_info=motherboard_info,
            processor_info=processor_info,
            storage_info=storage_info,
            free_space_c=free_space_c,
            user=user,  # Добавьте пользователя к записи
            timestamp=timezone.now()
        )

        return JsonResponse({"status": "success"})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)




def cartridge_list_api(request):
    cartridges = Cartridge.objects.all()
    data = [{'id': cartridge.id, 'name': cartridge.name, 'number': cartridge.number, 'status': cartridge.status} for cartridge in cartridges]
    return JsonResponse(data, safe=False)