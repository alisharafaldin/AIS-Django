from django.shortcuts import render, redirect
from django.contrib import messages
from employees.models import *
from .models import *
from basicinfo.models import Persons
from basicinfo.forms import PersonForm
from .forms import ShareholderForm, ContractsForm


# Create your views here.

def contract_print_pdf(request, contract_id):
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
    return render(request , 'hadena/contract_print.html', context)
 
def shareholders(request): 
  shareholders = ShareholdersInfo.objects.all()
  txtsearch = None
  if 'search_name' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['search_name'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          shareholders = shareholders.filter(f_Name_ar__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  if 'search_id_number' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['search_id_number'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          shareholders = shareholders.filter(id_number__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  if 'search_mobileNumber' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['search_mobileNumber'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          shareholders = shareholders.filter(mobileNumber__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  if 'typeID' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['typeID'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          shareholders = shareholders.filter(typeID=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  if 'workTradeID' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['workTradeID'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          shareholders = shareholders.filter(workTradeID=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف  
  context = {
      'shareholders':shareholders,
      'shar_form':ShareholderForm(),
  }
  return render(request, 'hadena/shareholders.html', context)

def shareholder_create(request): 
  if request.method == 'POST':
    supervisorID = None
    #Get Values from the form
    if 'supervisorID' in request.POST: supervisorID = request.POST['supervisorID']
    else: messages.error(request, 'Error in supervisorID')
    newPerson = PersonForm(request.POST, request.FILES)
    if newPerson.is_valid():
      newPerson.save()
      new_shareholder = ShareholdersInfo(personID=newPerson.instance, supervisorID_id=supervisorID)
      new_shareholder.save()
      messages.success(request, 'تمت الإضافة بنجاح') 
      return redirect('shareholders')
    else :      
      messages.error(request, 'خطأ في البيانات') 
      return redirect('shareholder_create')
  context = {
    'share_form': ShareholderForm(),
    'person_form': PersonForm(),
  }
  return render(request , 'hadena/shareholder_create.html', context)

def shareholder_FG(request): 
  return render(request , 'hadena/shareholder_FG.html')

def shareholder_reade(request, id):
    shareholder_reade = ShareholdersInfo.objects.get(id=id)
    context = {
        'shareholder_reade':shareholder_reade,
    }
    return render(request, 'hadena/shareholder_reade.html', context)

def shareholder_update(request, id):
  shareholder_update = ShareholdersInfo.objects.get(id=id)
  update_person = Persons.objects.get(id=shareholder_update.personID_id)
  update_share_form = ShareholderForm(instance=shareholder_update)
  update_person_form = PersonForm(request.POST, request.FILES, instance=update_person)
  if request.method == 'POST':
    supervisorID = None
    if 'supervisorID' in request.POST: supervisorID = request.POST['supervisorID']
    else: messages.error(request, 'Error in supervisorID')
    if update_person_form.is_valid():
      update_person_form.save()
      # update_share.supervisorID.pk=supervisorID 
      messages.success(request, 'تم تحديث البيانات بنجاح')       
      return redirect('shareholders') 
    else:
      messages.error(request, 'خطأ في تحديث البيانات بنجاح')       
      return redirect('shareholder_update') 
  update_person_form = PersonForm(instance=update_person)
  context = {
    'shareholder_update': shareholder_update,
    'shareholders': shareholder_update,
    'share_form': update_share_form,
    'person_form': update_person_form,
  }
  return render(request, 'hadena/shareholder_update.html', context)
  # return redirect('shareholders/contract/' + str(contract_id), context)

def shareholder_delete(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    delete_share = ShareholdersInfo.objects.get(id=id)
    if request.method == 'POST':
      delete_share.delete()
      messages.success(request, 'تم الحذف بنجاح')
      return redirect('shareholders')
  else:
      messages.error(request, 'خطأ في البيانات بنجاح')       
      return redirect('delete_share')
  context = {
      'person_form':delete_share,
  }
  return render(request, 'hadena/shareholder_delete.html', context)
  # return redirect('shareholders') 

def contract_create(request):
  if request.method == 'POST':
    contract_new = ContractsForm(request.POST, request.FILES)
    if contract_new.is_valid():
      contract_new.save()
      messages.success(request, 'تمت الإضافة بنجاح') 
      return redirect('contracts')
    else :      
      messages.error(request, 'خطأ في البيانات') 
      return redirect('contract_create')
  context = {
    'contract_form': ContractsForm(),
  }
  return render(request, 'hadena/contract_create.html', context)

def contract_reade(request, id):
    contract_reade = Contracts.objects.get(id=id)
    context = {
        'contract_reade':contract_reade,
        'totalamountOfShare': contract_reade.amountOfShare * contract_reade.numberOfShares
    }
    return render(request, 'hadena/contract_reade.html', context)

def contract_update(request, id):
  contract_update = Contracts.objects.get(id=id)
  contract_update_form = ContractsForm(request.POST, request.FILES, instance=contract_update)
  if request.method == 'POST':
    if contract_update_form.is_valid():
      contract_update_form.save()
      messages.success(request, 'تم تحديث البيانات بنجاح')       
      return redirect('contracts') 
    else:
      messages.error(request, 'خطأ في تحديث البيانات بنجاح')       
      return redirect('contract_updatet') 
  contract_update_form = ContractsForm(instance=contract_update)
  context = {
    'contract_update':contract_update,
    'contract_form':contract_update_form,
  }
  return render(request, 'hadena/contract_update.html', context)
  # return redirect('shareholders/contract/' + str(contract_id), context)

def contract_delete(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    contract_delete = Contracts.objects.get(id=id)
    if request.method == 'POST':
      contract_delete.delete()
      messages.success(request, 'تم الحذف بنجاح')
      return redirect('contracts')
  else:
    messages.error(request, 'خطأ في البيانات بنجاح')       
    return redirect('contract_delete')
  context = {
    'contract':contract_delete,
  }
  return render(request, 'hadena/contract_delete.html', context)
  # return redirect('shareholders') 

def contracts(request):
  contracts = Contracts.objects.all()
  contracts_form = ContractsForm()
    # Start Search
  txtsearch = None
  if 'search_shareholdersID' in request.GET: # للتحقق من وجود نيم  في الرابط
      txtsearch = request.GET['search_shareholdersID'] # تغذية المتغير بالمدخلات حسب النيم
      if txtsearch: # للتحقق أن البيانات ليست فارغة
          contracts = contracts.filter(shareholdersID__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  if 'search_contractNumber' in request.GET: # للتحقق من وجود نيم  في الرابط
        txtsearch = request.GET['search_contractNumber'] # تغذية المتغير بالمدخلات حسب النيم
        if txtsearch: # للتحقق أن البيانات ليست فارغة
            contracts = contracts.filter(contractNumber__icontains=txtsearch) #فلتر البيانات بالإسم من غير مراعات حساسية الأحرف 
  context = {
    'contracts':contracts,
    'contracts_form':contracts_form,
  }
  return render(request, 'hadena/contracts.html', context)

def contract_print(request, id):
    contract_reade = Contracts.objects.get(id=id)
    context = {
        'contract_reade':contract_reade,
        'totalamountOfShare': contract_reade.amountOfShare * contract_reade.numberOfShares
    }
    return render(request, 'hadena/contract_print.html', context)



