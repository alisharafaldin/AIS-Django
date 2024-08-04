
# class infoGeneral(models.Model):
#     nationalityID = models.ForeignKey(Countries, related_name='nationalityID', default=1, verbose_name='الجنسية', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     countryID = models.ForeignKey(Countries, related_name='countryID', default=1, verbose_name='بلد الإقامة', on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     regionID = models.ForeignKey(Region, verbose_name='المنطقة', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     stateID = models.ForeignKey(States, verbose_name='الولاية', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     cityID = models.ForeignKey(Cities, verbose_name='المدينة', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     desAddress = models.CharField(verbose_name='وصف العنوان',max_length=100, blank=True, null=True)
#     google_maps_location = models.URLField(verbose_name='العنوان على خرائط قوقل', max_length=500, blank=True, null=True)
#     phone = models.CharField(verbose_name='رقم الهاتف',max_length=100, blank=True, null=True)
#     phoneOther = models.CharField(verbose_name='رقم هاتف آخر',max_length=100, blank=True, null=True)
#     email = models.EmailField(verbose_name='البريد الإلكتروني',max_length=100, blank=True, null=True)
#     bankID = models.ForeignKey(Bank, verbose_name='البنك', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     branchBankID = models.ForeignKey(BranchBank, verbose_name='فرع البنك', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     typeAccBankID = models.ForeignKey(TypeAccBank, verbose_name='نوع الحساب', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     accountNumber = models.CharField(verbose_name='رقم الحساب المصرفي',max_length=100, blank=True, null=True)
#     IBANNumber = models.CharField(verbose_name='رقم الآيبان المصرفي',max_length=100, blank=True, null=True)
#     ownerAccount = models.CharField(verbose_name='إسم صاحب الحساب',max_length=100, blank=True, null=True)
#     photo = models.ImageField(verbose_name='صورة شخصية', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
#     notes = models.TextField(verbose_name='ملاحظات', blank=True, null=True)
#     attachments = models.FileField(verbose_name='مرفقات', blank=True, null=True)
#     documentLink = models.CharField(verbose_name='رابط المستندات',max_length=100, blank=True, null=True)
#     active = models.BooleanField(default=False, verbose_name="نشط", blank=True, null=True)
#     created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by', blank=True, null=True)
#     created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
#     updated_by = models.ForeignKey(User, verbose_name='المُعدِل', related_name='updated_by', on_delete=models.PROTECT, blank=True, null=True)
#     updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)


# class LegalPersons(models.Model):
#     name_ar = models.CharField(verbose_name='الإسم عربي',max_length=100)
#     acronym_ar = models.CharField(verbose_name='الإسم المختصر عربي',max_length=100, blank=True, null=True)
#     name_en = models.CharField(verbose_name='الإسم إنجليزي',max_length=100, blank=True, null=True)
#     acronym_en = models.CharField(verbose_name='الإسم المختصر إنجليزي',max_length=100, blank=True, null=True)
#     who_are_we = models.TextField(verbose_name='من نحن', max_length=250, blank=True, null=True)
#     businessTypeID = models.ForeignKey(BusinessType, default=1, verbose_name='نوع الشركة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     countryID = models.ForeignKey(Countries, default=13, verbose_name='الدولة',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     regionID = models.ForeignKey(Region, verbose_name='المنطقة', on_delete=models.PROTECT, blank=True, null=True)
#     stateID = models.ForeignKey(States, verbose_name='الولاية', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     cityID = models.ForeignKey(Cities, verbose_name='المدينة', default=1, on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     address = models.CharField(verbose_name='وصف عنوان مقر الشركة',max_length=100, blank=True, null=True)
#     google_maps_location = models.URLField(verbose_name='العنوان على خرائط قوقل', max_length=500, blank=True, null=True)
#     bankID = models.ForeignKey(Bank, verbose_name='البنك',on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     branchBankID = models.ForeignKey(BranchBank, verbose_name='فرع البنك', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     typeAccBankID = models.ForeignKey(TypeAccBank, verbose_name='نوع الحساب', default=1,on_delete=models.PROTECT, blank=True, null=True) #لن يتم حزف الصنف في حالة حذف الموظف
#     accountNumber = models.CharField(verbose_name='رقم الحساب المصرفي',max_length=100, blank=True, null=True)
#     IBANNumber = models.CharField(verbose_name='رقم الآيبان المصرفي',max_length=100, blank=True, null=True)
#     accountName = models.CharField(verbose_name='حساب البنك بإسم',max_length=100, blank=True, null=True)
#     phone = models.CharField(verbose_name='رقم الهاتف',max_length=100, blank=True, null=True)
#     phoneOther = models.CharField(verbose_name='رقم هاتف آخر',max_length=100, blank=True, null=True)
#     email = models.CharField(verbose_name='البريد الإلكتروني',max_length=100, blank=True, null=True)
#     website = models.CharField(verbose_name='الموقع الإلكتروني',max_length=100, blank=True, null=True)
#     fax = models.CharField(verbose_name='فاكس',max_length=100, blank=True, null=True)
#     POBox = models.CharField(verbose_name='صندوق بريد',max_length=100, blank=True, null=True)
#     administrator = models.CharField(verbose_name='الموظف المسؤول',max_length=100, blank=True, null=True)
#     logo = models.ImageField(verbose_name='شعار الشركة', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
#     taxNumber = models.CharField(verbose_name='الرقم الضريبي',max_length=100, blank=True, null=True)
#     active = models.BooleanField(default=False, verbose_name="نشط", blank=True, null=True)
#     notes = models.CharField(verbose_name='ملاحظات',max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(verbose_name='تاريخ الإنشاء',auto_now_add=True, blank=True, null=True)
#     updated_at = models.DateTimeField(verbose_name='تاريخ التعديل', auto_now=True, blank=True, null=True)

#     def __str__(self):
#         return str(self.name_ar)

#     class MPTTMeta:
#         order_insertion_by = ['name_ar']

#     def __str__(self):
#         return str(self.name_ar)
    
# class Person(models.Model):