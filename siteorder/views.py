from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from siteorder.forms import TariffPlanForm, PaymentForm, SiteForm

from .models import Site, TariffPlan, Payment

from django.http import HttpResponse
from .second_telegram_bot import main_second_bot, notify_users_second_bot


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправлення до списку сайтів
    else:
        form = SiteForm()
    return render(request, 'siteorder/add_site.html', {'form': form})


def site_list(request):
    sites = Site.objects.all()
    tariff_plans = TariffPlan.objects.all()
    payments = Payment.objects.all()
    return render(request, 'siteorder/site_list.html', {
        'sites': sites,
        'tariff_plans': tariff_plans,
        'payments': payments
    })

def add_tariff(request):
    if request.method == 'POST':
        form = TariffPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправлення до списку сайтів
    else:
        form = TariffPlanForm()
    return render(request, 'siteorder/add_tariff.html', {'form': form})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправлення до списку сайтів
    else:
        form = PaymentForm()
    return render(request, 'siteorder/add_payment.html', {'form': form})


def edit_site(request, pk):
    """
    Відображає форму для редагування сайту.
    """
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправлення до списку сайтів
    else:
        form = SiteForm(instance=site)
    return render(request, 'siteorder/edit_site.html', {'form': form})

def edit_payment(request, pk):
    """
    Відображає форму для редагування оплати.
    """
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправлення до списку оплат
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'siteorder/edit_payment.html', {'form': form})



def site_detail(request, pk):
    """
    Відображає детальну інформацію про сайт.
    """
    site = get_object_or_404(Site, pk=pk)
    return render(request, 'siteorder/site_detail.html', {'site': site})

def payment_detail(request, pk):
    """
    Відображає детальну інформацію про оплату.
    """
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'siteorder/payment_detail.html', {'payment': payment})

def tariff_detail(request, pk):
    """
    Відображає детальну інформацію про тарифний план.
    """
    tariff_plan = get_object_or_404(TariffPlan, pk=pk)
    return render(request, 'siteorder/tariff_detail.html', {'tariff_plan': tariff_plan})

def delete_site(request, pk):
    site = get_object_or_404(Site, pk=pk)
    site.delete()
    return redirect('site_list')

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('site_list')

def delete_tariff(request, pk):
    tariff_plan = get_object_or_404(TariffPlan, pk=pk)
    tariff_plan.delete()
    return redirect('site_list')


def edit_tariff(request, pk):
    """
    Відображає форму для редагування тарифного плану.
    """
    tariff_plan = get_object_or_404(TariffPlan, pk=pk)
    if request.method == 'POST':
        form = TariffPlanForm(request.POST, instance=tariff_plan)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Перенаправлення до списку сайтів
    else:
        form = TariffPlanForm(instance=tariff_plan)
    return render(request, 'siteorder/edit_tariff.html', {'form': form})


def get_tariff_price(request):
    site_id = request.GET.get('site_id')
    if site_id:
        try:
            site = Site.objects.get(pk=site_id)
            tariff_price = site.tariff_plan.price if site.tariff_plan else None
            return JsonResponse({'price': tariff_price})
        except Site.DoesNotExist:
            return JsonResponse({'price': None})
    return JsonResponse({'price': None})


def run_second_bot(request):
    # Виклик головної функції другого бота
    main_second_bot()
    return HttpResponse("Другий бот запущений")

def send_message_to_user_second_bot(request):
    # Виклик функції надсилання повідомлення від другого бота
    notify_users_second_bot("Це тестове повідомлення від другого Django бота!")
    return HttpResponse("По відомлення надіслано другим ботом")