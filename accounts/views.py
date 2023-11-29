
from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from . models import AccountsTree , Qayd ,QaydDetails
from employees.models import EmpInfo
from . forms import AccountsTreeForm, QaydForm, QaydDetailsForm
from django.utils import timezone
from django.forms import modelformset_factory

def account_create(request):
    if request.method == 'POST':
        add_acc = AccountsTreeForm(request.POST, request.FILES)
        if add_acc.is_valid():
            add_acc.save()
            messages.success(request, 'تمت الإضافة بنجاح') 
    context = {
        'acc_form': AccountsTreeForm(),
    }    
    return render(request,'accounts/account_create.html', context)

def account_reade(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      account_id = AccountsTree.objects.get(id=id)
    context = {
        'account':account_id,
    }
    return render(request, 'accounts/account_reade.html', context)

def account_update(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        account_id = AccountsTree.objects.get(id=id)
        if request.method == 'POST':
            account_save = AccountsTreeForm(request.POST, request.FILES, instance=account_id)
            if account_save.is_valid():
                account_save.save()
                messages.success(request, 'تم التحديث بنجاح')       
                return redirect('accounts')
        else:
            account_save = AccountsTreeForm(instance=account_id)
        context = {
            'account_form':account_save,
            'account':account_id,
        }
        return render(request, 'accounts/account_update.html', context)
    else:
        messages.info(request, 'الرجاء تسجيل الدخول' )
        return redirect('accounts')

def account_delete(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      account_id = AccountsTree.objects.get(id=id)
      if 'btndelete' in request.POST:
        account_id.delete()
        messages.info(request, 'تم الحذف بنجاح')
        return redirect('accounts')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    context = {
        'account':account_id,
    }
    return render(request, 'accounts/account_delete.html', context)

def accounts(request):
    accounts = AccountsTree.objects.all().order_by("typeID")
    accounts2 = accounts.order_by("code")
    context = {
        'accounts':accounts2,
    }    
    return render(request,'accounts/accounts.html', context)

def qayd_create(request):
  if request.method == 'POST':
    # if 'date' in request.POST: date = request.POST['date']
    # else: messages.error(request, 'Error in date')
    # if 'rate' in request.POST: rate = request.POST['rate']
    # else: messages.error(request, 'Error in rate')
    # if 'currencyID' in request.POST: currencyID = request.POST['currencyID']
    # else: messages.error(request, 'Error in currencyID')
    # if 'debit' in request.POST: debit = request.POST['debit']
    # else: messages.error(request, 'Error in debit')
    # if 'credit' in request.POST: credit = request.POST['credit']
    # else: messages.error(request, 'Error in credit')
    # if 'description' in request.POST: description = request.POST['description']
    # else: messages.error(request, 'Error in description')
    # if 'accountID' in request.POST: accountID = request.POST['accountID']
    # else: messages.error(request, 'Error in accountID')
    # if 'projectID' in request.POST: projectID = request.POST['projectID']
    # else: messages.error(request, 'Error in ')
    # if 'empID' in request.POST: empID = request.POST['empID']
    # else: messages.error(request, 'Error in empID')
    qayd = QaydForm(request.POST, request.FILES)
    if qayd.is_valid():
      qayd.save()
      # qayd_details = QaydDetails()
      # qayd_details.qaydID=qayd.instance
      # qayd_details.date = request.POST['date']
      # qayd_details.rate = request.POST['rate']
      # qayd_details.debit = request.POST['debit']
      # qayd_details.credit = request.POST['credit']
      # qayd_details.description = request.POST['description']
      # qayd_details.accountID = request.POST['accountID']
      # qayd_details.currencyID = request.POST['currencyID']
      # qayd_details.projectID = request.POST['projectID']
      # qayd_details.empID = request.POST['empID']
      # qayd_details.save()
      messages.success(request, 'تمت الإضافة بنجاح') 
      return redirect('qayds')
    else :      
      messages.error(request, 'خطأ في البيانات') 
      return redirect('qayd_create')

  context = {
      'all_qayd': Qayd.objects.all(),
      'qayd_form': QaydForm(),
      'qayd_details_form': QaydDetailsForm(),
  }    
  return render(request,'accounts/qayd_create.html', context)

def qayd_reade(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    qayd_id = Qayd.objects.get(id=id)
    qayd_id_details = QaydDetails.objects.filter(qaydID=id)
    class calc:
      total_d = 0
      total_c = 0
      other = 0
      for td in qayd_id_details:
        total_d += td.debit 
        total_c += td.credit 
        other = total_d - total_c
    context = {
        'qayd_id':qayd_id,
        'qayd_id_details':qayd_id_details,
        # 'total_d':total_d,
        # 'total_c':total_c,
        'calc':calc,
    }
    return render(request, 'accounts/qayd_reade.html', context)

# def qayd_update(request, id):
#     qayd_update = Qayd.objects.get(id=id)
#     qayd_update_details = modelformset_factory(QaydDetails, fields=('qaydID',))
#     formset = qayd_update_details(queryset=QaydDetails.objects.filter(qaydID=id))
#     context = {
#       'qayd_update':formset,
#     }
#     return render(request, 'accounts/qayd_update.html', context)

def qayd_update(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    qayd_update = Qayd.objects.get(id=id)
    qayd_update_form = QaydForm(request.POST, request.FILES, instance=qayd_update)
    qayd_update_details = QaydDetails.objects.get(qaydID=id)
    qayd_update_details_form = QaydDetailsForm(request.POST, request.FILES, instance=qayd_update)
    if 'btnsave' in request.POST:
      if request.method == 'POST':
        qayd_update.userID = request.user
        qayd_update.date = request.POST['date']
        qayd_update.descrpition = request.POST['description']
        qayd_update.typeTransactionID_id = request.POST['typeTransactionID']
        qayd_update.attachments = request.POST['attachments']  
        qayd_update.save()
        # if qayd_update_details_form.is_valid():
        # qayd_update_details_form.save()
        qayd_update_details.accountID_id = request.POST['accountID']
        qayd_update_details.debit = request.POST['debit']
        qayd_update_details.credit = request.POST['credit']
        qayd_update_details.description = request.POST['description']
        qayd_update_details.projectID_id = request.POST['projectID']
        qayd_update_details.empID_id = request.POST['empID']
        qayd_update_details.save()
        messages.success(request, 'تم التحديث بنجاح')
        return redirect('qayds')
      else:
        messages.error(request, 'خطأ في البيانات')   
    qayd_update_form = QaydForm(instance=qayd_update)
    qayd_update_details_form = QaydDetailsForm(instance=qayd_update_details)
    class calc:
      qdd = QaydDetails.objects.filter(qaydID=id)
      total_d = 0
      total_c = 0
      other = 0
      for td in qdd:
        total_d += td.debit 
        total_c += td.credit 
        other = total_d - total_c
    context = {
        'qayd_update':qayd_update,
        'qayd_update_form':qayd_update_form,
        'qayd_update_details':qayd_update_details,
        'qayd_update_details_form':qayd_update_details_form,
        'calc':calc,
    }
    return render(request, 'accounts/qayd_update.html', context)
  else:
    messages.info(request, 'الرجاء تسجيل الدخول')
    return redirect('signin')    

def qayd_delete(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      qayd_id = Qayd.objects.get(id=id)
      if 'btndelete' in request.POST:
        qayd_id.delete()
        messages.info(request, 'تم الحذف بنجاح')
        return redirect('qayds')
    else:
        messages.error(request, 'الرجاء تسجيل الدخول أولاً')
    qayd_id_details = QaydDetails.objects.filter(qaydID=id)
    class calc:
      total_d = 0
      total_c = 0
      other = 0
      for td in qayd_id_details:
        total_d += td.debit 
        total_c += td.credit 
        other = total_d - total_c
    context = {
        'qayd_id':qayd_id,
        'qayd_id_details':qayd_id_details,
        # 'total_d':total_d,
        # 'total_c':total_c,
        'calc':calc,
    }
    return render(request, 'accounts/qayd_delete.html', context)

def qayds(request):
    context = {
        'qayds':Qayd.objects.all(),
    }
    return render(request,'accounts/qayds.html', context)