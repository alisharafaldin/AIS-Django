from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employees.models import *
from .models import *
from django.views.generic import CreateView
from .forms import ShareholderForm, ContractsForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

def shareholders(request):
    if request.method == 'POST':
        add_share = ShareholderForm(request.POST, request.FILES)
        if add_share.is_valid():
            add_share.save()
            messages.success(request, 'تمت الإضافة بنجاح')
    all_share = ShareholdersInfo.objects.all()
     # Start Search
    txtsearch = None
    if 'search_name' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_name'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_share = all_share.filter(f_Name_ar__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'search_id_number' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_id_number'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_share = all_share.filter(id_number__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'search_mobileNumber' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_mobileNumber'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_share = all_share.filter(mobileNumber__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    context = {
        'shar_form':ShareholderForm(),
        'all':all_share,
    }
    return render(request , 'shareholders/shareholders.html', context)

def contracts(request):
    if request.method == 'POST':
        add_contract = ContractsForm(request.POST, request.FILES)
        if add_contract.is_valid():
            add_contract.save()
            messages.success(request, 'تمت الإضافة بنجاح')
    all_contract = Contracts.objects.all()
     # Start Search
    txtsearch = None
    if 'search_name' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_name'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_contract = all_contract.filter(f_Name_ar__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'search_id_number' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_id_number'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_contract = all_contract.filter(id_number__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    if 'search_mobileNumber' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_mobileNumber'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            all_contract = all_contract.filter(mobileNumber__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
    context = {
        'contract_form':ContractsForm(),
        'all_contract':all_contract,
    }
    return render(request , 'shareholders/contracts.html', context)

def contract(request, contract_id):
    # if request.user.is_authenticated:
    all_contract = Contracts.objects.all()
    contract = Contracts.objects.get(id=contract_id)
    totalamountOfShare = contract.amountOfShare * contract.numberOfShares
    context = {
        'contract':contract,
        'all_contract':all_contract,
        'totalamountOfShare':totalamountOfShare,
    }
    return render(request , 'shareholders/contract.html', context)

def contract_print(request, contract_id):
     # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def update(request, contract_id):
    contract_id = Contracts.objects.get(id=contract_id)
    if request.method == 'POST':
        contract_save = ContractsForm(request.POST, request.FILES, instance=contract_id)
        if contract_save.is_valid():
            contract_save.save()
            messages.success(request, 'تم تحديث البيانات بنجاح')       
    else:
        contract_save = ContractsForm(instance=contract_id)
    context = {
        'contract_form':contract_save,
        'contract':contract_id,
    }
    return render(request, 'shareholders/update.html', context)
    # return redirect('shareholders/contract/' + str(contract_id), context)
