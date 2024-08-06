    if request.method == 'POST':
      basicInfo_form = BasicInfoForm(request.POST, request.FILES)
      legalPerson_form = LegalPersonsForm(request.POST, request.FILES)
      customer_form = CustomerForm(request.POST, request.FILES)

      if basicInfo_form.is_valid() and legalPerson_form.is_valid() and customer_form.is_valid():

        basicInfo = basicInfo_form.save(commit=False)
        basicInfo.created_by = request.user  # تعيين created_by فقط عند إنشاء قيد جديد
        basicInfo.save()

        legalPerson = legalPerson_form.save(commit=False)
        legalPerson.basicInfoID = basicInfo
        legalPerson.save()

        # التحقق من وجود current_company_id في الجلسة قبل استخدامه.
        current_company_id = request.session.get('current_company_id')
        if not current_company_id:
            messages.error(request, 'لم يتم تحديد الشركة الحالية.')
            return redirect('sales')
        
        customer = customer_form.save(commit=False)
        customer.companyID = get_object_or_404(Company, id=current_company_id)
        customer.legalPersonID = legalPerson
        customer.save()
        messages.success(request, f'تم إضافة عميل جديد بإسم : {customer.legalPersonID.name_ar}')
        return redirect('customers')
      else:
        # دالة عرض الأخطاء
        handle_form_errors(legalPerson_form, customer_form, request)
        # إعادة عرض النماذج مع الأخطاء
        return render(request, 'sales/customer_create.html', {
            'basicInfo_form': basicInfo_form,
            'legalPerson_form': legalPerson_form,
            'customer_form': customer_form,
        })
    else:
        # إعداد النماذج عند طلب GET
        basicInfo_form = BasicInfoForm()
        legalPerson_form = LegalPersonsForm()
        customer_form = CustomerForm()
    context = {
       'basicInfo_form': basicInfo_form,
       'legalPerson_form': legalPerson_form,
       'customer_form': customer_form,

       'basicInfo_label': basicInfo_form,
       'legalPerson_label': legalPerson_form,
       'customer_label': customer_form,
    }
    return render(request, 'sales/invoice_create.html', context)

