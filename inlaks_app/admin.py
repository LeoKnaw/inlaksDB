from django.contrib import admin
from .models import ATM, Service
# Register your models here.

admin.site.site_header = 'Inlaks Dashboard Admin'

class AtmFields(admin.ModelAdmin):
    list_display = (ATM , 'acc_num', 'date_of_transaction', 'atm_or_pos', 'status')


class ServiceFields(admin.ModelAdmin):
    list_display = ('name','is_online')


admin.site.register(ATM, AtmFields)
admin.site.register(Service, ServiceFields)