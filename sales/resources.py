# from import_export import resources, fields
# from import_export.widgets import ForeignKeyWidget
# from basicinfo.models import BasicInfo, LegalPersons
# from .models import Customers


# class BasicInfoResource(resources.ModelResource):
#     class Meta:
#         model = BasicInfo
#         fields = '__all__'

# class LegalPersonsResource (resources.ModelResource):
#   class Meta:
#       model = LegalPersons
#       fields = '__all__'

# class CustomerResource(resources.ModelResource):
#     # الحصول على BasicInfo عبر LegalPersons
#     basic_info = fields.Field(
#         column_name='basicInfoID',
#         attribute='legalPersonID__basicInfoID',  # التعامل مع العلاقة عبر LegalPersons
#         widget=ForeignKeyWidget(BasicInfo, 'id'))

#     legal_persons = fields.Field(
#         column_name='legalPersonID',
#         attribute='legalPersonID',
#         widget=ForeignKeyWidget(LegalPersons, 'id'))

#     class Meta:
#         model = Customers
#         fields = ('id', 'basic_info', 'legal_persons', 'name', 'address')  # تخصيص الحقول التي تحتاجها