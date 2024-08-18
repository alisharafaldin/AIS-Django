from rest_framework import serializers
from .models import Customers
from basicinfo.models import LegalPersons

class LegalPersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPersons
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    legalPersonID = LegalPersonsSerializer()  # لجلب البيانات من الجدول المرتبط

    class Meta:
        model = Customers
        fields = '__all__'
  # أضف الحقول الأخرى التي تريد إرجاعها