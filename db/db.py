import os
import django
import csv
from django.core.management import BaseCommand


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ais.settings')  # استبدل 'your_project_name' باسم مشروعك
django.setup()

import pandas as pd
from basicinfo.models import *  # استبدل your_app و YourModel باسم تطبيقك ونموذجك
from companys.models import *
from employees.models import *
from profiles.models import *
from inventorys.models import *
from products.models import *
from purchases.models import *
from sales.models import *
# استعلام البيانات
# إنشاء قائمة بالجداول
models = {
    #1- App.basicinfo
    'Countries': Countries,
    'Region': Region,
    'States': States,
    'Cities': Cities,
    'CalendarYears': CalendarYears,
    'CalendarMonths': CalendarMonths,
    'CalendarWeek': CalendarWeek,
    'Gender': Gender,
    'SocialStatus': SocialStatus,
    'WorkTrade': WorkTrade,
    'WorkSpecialty': WorkSpecialty,
    'JobTitle':JobTitle ,
    'WorkingStatus': WorkingStatus,
    'Bank': Bank,
    'BranchBank': BranchBank,
    'TypeAccBank': TypeAccBank,
    'TypeID': TypeID,
    'TypeTransaction': TypeTransaction,
    'TargetGroup': TargetGroup,
    'BusinessType': BusinessType,
    'BusinessScope': BusinessScope,
    'BusinessScopeSpecialization': BusinessScopeSpecialization,
    'Project': Project,
    'SubProject': SubProject,
    'Size': Size,
    'Color': Color,
    'Languages': Languages,
    'Skills': Skills,
    'TypeDelivery': TypeDelivery,
    'TypePayment': TypePayment,
    'TypeUnit': TypeUnit,
    'BasicInfo': BasicInfo,
    'LegalPersons': LegalPersons,
    'Persons': Persons,
    #2- App.companys
    'Company': Company,
    'CompanyUser': CompanyUser,
    #3- App.employees
    'Employee': Employee,
    'ProjectRotation': ProjectRotation,
    #4- App.inventorys
    'inventory': Inventory,
    #5- App.products
    'ItemGrop': ItemGrop,
    'ItemType': ItemType,
    'ItemType': Items,
    #6- App.purchases
    'Suppliers': Suppliers,
    'InvoicesPurchasesHead': InvoicesPurchasesHead,
    'InvoicesPurchasesBody': InvoicesPurchasesBody,
    #7- App.sales
    'Customers': Customers,
    'InvoicesSalesHead': InvoicesSalesHead,
    'InvoicesSalesBody': InvoicesSalesBody,
}

def to_xlsx():
    # تحديد مسار حفظ الملفات
    save_directory = 'd:/AIS-Django/db-exports_to_xlsx/'  # تأكد من أن هذا المجلد موجود

    # تهيئة ترقيم الملفات
    num = 0
    # تكرار الجداول وتصدير البيانات
    for model_name, model in models.items():
        num += 1  # زيادة الرقم في كل تكرار
        # الحصول على البيانات
        data = model.objects.all().values()  # استخدم values() للحصول على القيم كقاموس
        # تحويل البيانات إلى DataFrame
        df = pd.DataFrame(data)
        
        # معالجة الأعمدة الزمنية إذا كانت موجودة
        for col in df.select_dtypes(include=['datetime64[ns, UTC]', 'datetime64[ns]']).columns:
            df[col] = df[col].dt.tz_localize(None)  # إزالة المنطقة الزمنية
        
        # تصدير البيانات إلى ملف Excel
        filename = f'{num} - {model_name}.xlsx'  # اسم الملف يعتمد على اسم النموذج
        file_path = os.path.join(save_directory, filename)  # دمج المسار مع اسم الملف
        df.to_excel(file_path, index=False, engine='openpyxl')  # استخدم engine='openpyxl' لتصدير إلى Excel

    print("All tables exported successfully!")

def to_csv():
    # المسار لحفظ ملفات CSV
    save_directory = 'd:/AIS-Django/db-exports_to_csv/'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # تصدير البيانات إلى ملفات CSV
    for num, (model_name, model) in enumerate(models.items(), start=1):
        data = model.objects.all().values()
        df = pd.DataFrame(data)

        filename = f'{num} - {model_name}.csv'
        file_path = os.path.join(save_directory, filename)

        # تصدير إلى CSV
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"{filename} exported successfully.")

    print("All tables exported successfully!")


# to_xlsx()
to_csv()