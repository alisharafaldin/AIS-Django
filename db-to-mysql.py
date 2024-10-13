import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ais.settings')  # استبدل 'your_project_name' باسم مشروعك
django.setup()

import pandas as pd
from basicinfo.models import *  # استبدل your_app و YourModel باسم تطبيقك ونموذجك
from companys.models import *
from employees.models import *
from profiles.models import *
from sqlalchemy import create_engine

# استعلام البيانات
# إنشاء قائمة بالجداول
models = {
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
}

# إعداد الاتصال بقاعدة بيانات MySQL
db_config = {
    'user': 'alisharafaldinal',  # استبدل باسم المستخدم الخاص بك
    'password': 'asa13579@MA01',  # استبدل بكلمة المرور الخاصة بك
    'host': 'alisharafaldinali.mysql.pythonanywhere-services.com',  # أو عنوان السيرفر الخاص بك
    'port': '3306',  # المنفذ الافتراضي لقاعدة بيانات MySQL
    'database': 'alisharafaldinal$aisdb',  # استبدل باسم قاعدة البيانات الخاصة بك
}

# إعداد سلسلة الاتصال
connection_string = f"mysql+mysqldb://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(connection_string)

# تهيئة ترقيم الملفات
num = 0

# تكرار الجداول واستيراد البيانات
for model_name, model in models.items():
    num += 1  # زيادة الرقم في كل تكرار
    # الحصول على البيانات
    data = model.objects.all().values()  # استخدم values() للحصول على القيم كقاموس
    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(data)
    
    # معالجة الأعمدة الزمنية إذا كانت موجودة
    for col in df.select_dtypes(include=['datetime64[ns, UTC]', 'datetime64[ns]']).columns:
        df[col] = df[col].dt.tz_localize(None)  # إزالة المنطقة الزمنية
    
    # استيراد البيانات إلى قاعدة بيانات MySQL
    df.to_sql(model_name.lower(), con=engine, if_exists='append', index=False)  # استخدم if_exists='replace' إذا كنت تريد استبدال الجدول
    
print("All tables exported successfully!")