from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from employees.models import *
from .models import *
from basicinfo.models import Person
from basicinfo.forms import PersonForm
from django.views.generic import CreateView
from .forms import ShareholderForm, ContractsForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic import View
from .pdf import html2pdf

# Create your views here.

def pdf(request, contract_id):
    # if request.user.is_authenticated:
    all_contract = Contracts.objects.all()
    contract = Contracts.objects.get(id=contract_id)
    totalamountOfShare = contract.amountOfShare * contract.numberOfShares
    context = {
        'contract':contract,
        'all_contract':all_contract,
        'totalamountOfShare':totalamountOfShare,
    }
    # pdf=html2pdf("shareholders/pdf.html")
    # return HttpResponse(pdf, content_type='application/pdf')
    return render(request , 'hadena/pdf.html', context)
 
def shareholders(request): 
  all_share = ShareholdersInfo.objects.all()
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
  if 'typeID' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['typeID'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          all_share = all_share.filter(typeID=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  if 'workTradeID' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['workTradeID'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          all_share = all_share.filter(workTradeID=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف  
  context = {
      'shar_form':ShareholderForm(),
      'shareholders':all_share,
  }
  return render(request, 'hadena/shareholders.html', context)

def new_shareholder(request): 
    if request.method == 'POST':
      marketerID = None
      #Get Values from the form
      if 'marketerID' in request.POST: marketerID = request.POST['marketerID']
      else: messages.error(request, 'Error in marketerID')
      newPerson = PersonForm(request.POST, request.FILES)
      if newPerson.is_valid():
        newPerson.save()
        new_shareholder = ShareholdersInfo(personID=newPerson.instance, marketerID_id=marketerID)
        new_shareholder.save()
        messages.success(request, 'تمت الإضافة بنجاح') 
        return redirect('shareholders')
      else :      
        messages.error(request, 'خطأ في البيانات') 
        return redirect('new_shareholder')
    context = {
      'share_form': ShareholderForm(),
      'person_form': PersonForm(),
    }
    return render(request , 'hadena/new_shareholder.html', context)

def shareholder(request, shareholder_id):
    shareholders = ShareholdersInfo.objects.all()
    shareholder = ShareholdersInfo.objects.get(id=shareholder_id)
    context = {
        'shareholder':shareholder,
        'shareholders':shareholders,
    }
    return render(request , 'hadena/shareholder.html', context)

def share_update(request, shareholder_id):
    shareholder_id = ShareholdersInfo.objects.get(id=shareholder_id)
    if request.method == 'POST':
        shareholder_save = ShareholderForm(request.POST, request.FILES, instance=shareholder_id)
        if shareholder_save.is_valid():
            shareholder_save.save()
            messages.success(request, 'تم تحديث البيانات بنجاح')       
        return redirect('shareholders') 
    else:
        shareholder_save = ShareholderForm(instance=shareholder_id)
    context = {
        'shareholder_form':shareholder_save,
        'shareholder':shareholder_id,
    }
    return render(request, 'hadena/share_update.html', context)
    # return redirect('shareholders/contract/' + str(contract_id), context)

def share_delete(request, shareholder_id):
    if request.user.is_authenticated and not request.user.is_anonymous and shareholder_id:
        shareholder = ShareholdersInfo.objects.get(id=shareholder_id)
        shareholder.delete()
        messages.success(request, 'تم الحذف بنجاح')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول')
    # return render(request, 'shareholders/share_update.html', context)
    return redirect('shareholders') 

def contracts(request):
    if request.method == 'POST':
        add_contract = ContractsForm(request.POST, request.FILES)
        if add_contract.is_valid():
            add_contract.save()
            messages.success(request, 'تمت الإضافة بنجاح')
    all_contract = Contracts.objects.filter(shareholdersID__companyID=1)
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
    return render(request , 'hadena/contracts.html', context)

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
    # pdf=html2pdf("shareholders/contract.html")
    # return HttpResponse(pdf, content_type='application/pdf', context)
    return render(request , 'hadena/contract.html', context)

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
    return render(request, 'hadena/update.html', context)
    # return redirect('shareholders/contract/' + str(contract_id), context)
