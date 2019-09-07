from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from .models import ATM, Service
from django.db.models import Avg, Min, Max, Sum
from rest_framework import viewsets
from django.utils import timezone
from .serializers import ATMSerializer, ServiceSerializer
from datetime import date

# Create your views here.

class ATMView(viewsets.ModelViewSet):
    queryset = ATM.objects.all()
    serializer_class = ATMSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@login_required
def home(request):


    onlineService = (Service.objects.filter(is_online=True).count()/Service.objects.all().count()) * 100
    atm = (ATM.objects.filter(atm_or_pos=True).count()/ATM.objects.all().count()) * 100



    atmToday = ATM.objects.filter(atm_or_pos=True, date_of_transaction__day=timezone.now().day).aggregate(Sum('amount'))
    posToday = ATM.objects.filter(atm_or_pos=False, date_of_transaction__day=timezone.now().day).aggregate(Sum('amount'))
    success = ATM.objects.filter(status='Success', date_of_transaction__day=timezone.now().day).count()


    if success == 0:
        reverse = 0
    else:
        reverse = ATM.objects.filter(status='Reversed', date_of_transaction__day=timezone.now().day).count()/success * 100

    sumToday = ATM.objects.filter(date_of_transaction__day=timezone.now().day).aggregate(Sum('amount'))

    # while True:
    #     pass

    sumList = []

    context = {
        'average': ATM.objects.aggregate(Avg('amount'))['amount__avg'],
        'sum': ATM.objects.aggregate(Sum('amount'))['amount__sum'],
        'online': int(onlineService),
        'serviceDown':Service.objects.filter(is_online=False).count(),
        'atm': int(atm),
        'atmToday':atmToday['amount__sum'],
        'posToday':posToday['amount__sum'],
        'reverse':reverse,
        'recent':ATM.objects.last(),
        'sumToday':sumToday['amount__sum']

    }

    return render(request, 'inlaks_app/home.html', {'context':context})

def atm(request):


    return render(request, 'inlaks_app/atm.html')
