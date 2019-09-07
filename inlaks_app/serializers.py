from rest_framework import serializers
from .models import ATM, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("name", "is_online")


class ATMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATM
        fields = ("pan_number", "amount", "location", "acc_num", "date_of_transaction", "atm_or_pos")
