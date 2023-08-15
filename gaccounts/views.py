
from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from . models import AccountsTree , Qayd ,QaydDetails
from employees.models import EmpInfo
from . forms import AccountsTreeForm, QaydForm, QaydDetailsForm
from django.utils import timezone
from django.forms import modelform_factory

# Create your views here.

def acc_add(request):
    if request.method == 'POST':
        add_acc = AccountsTreeForm(request.POST, request.FILES)
        if add_acc.is_valid():
            add_acc.save()
            messages.success(request, 'تمت الإضافة بنجاح') 
    context = {
        'acc_form': AccountsTreeForm(),
        'acc_all':AccountsTree.objects.all(),  
    }    
    return render(request,'gaccounts/acc_all.html', context)

def acc_update(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        acc_id = AccountsTree.objects.get(id=id)
        if request.method == 'POST':
            acc_save = AccountsTreeForm(request.POST, request.FILES, instance=acc_id)
            if acc_save.is_valid():
                acc_save.save()
                messages.success(request, 'تمت تحديث البيانات بنجاح')       
                return redirect('acc_all')
        else:
            acc_save = AccountsTreeForm(instance=acc_id)
        context = {
            'acc_form':acc_save,
        }
        return render(request, 'gaccounts/acc_update.html', context)
    else:
        messages.info(request, 'الرجاء تسجيل الدخول' )
        return redirect('acc_all')

def qayd_all(request):    
    context = {
        'all_qayd':Qayd.objects.all(),
    }
    return render(request,'gaccounts/qayd_all.html', context)

def qayd_add(request):
    if request.method == 'POST':
      new_qayd = QaydForm(request.POST, request.FILES)
      new_qayd.userID = request.user
      if new_qayd.is_valid():
        new_qayd.save()
        messages.success(request, 'تمت إضافة القيد بنجاح')
        return redirect('qayd_all')    
      else:
        messages.error = (request, 'خطأ في راس القيد') 
    else:
      messages.error = (request, 'خطأ في تفاصيل القيد')
      # return redirect('qayd_all')    
    context = {
        'all_qayd': Qayd.objects.all(),
        'qayd_form': QaydForm(),
        # 'calc':calc,
        # 'qayd_details_form': QaydDetails(),
    }    
    return render(request,'gaccounts/qayd_add.html', context)

def new_qayd(request):
    if request.method == 'POST':
      # new_qayd = QaydForm(request.POST, request.FILES)
      new_qayd = Qayd()
      new_qayd.userID = request.user
      new_qayd.dateQayd = request.POST['dateQayd']
      new_qayd.desQayd = request.POST['desQayd']
      new_qayd.currencyID = request.POST['currencyID']
      new_qayd.attachments = request.POST['attachments']  
      new_qayd.save()
      qayddetails = QaydDetails()
      qayddetails.qaydID = new_qayd
      # qayddetails.accID = request.POST['accID']
      qayddetails.debit = request.POST['debit']
      qayddetails.credit = request.POST['credit']
      qayddetails.desQaydDetails = request.POST['desQaydDetails']
      # qayddetails.projectID = request.POST['projectID']
      # qayddetails.empID = request.POST['empID']
      qayddetails.save()
      messages.success(request, 'تمت إضافة القيد بنجاح')
      return redirect('qayd_all')    
    else:
        messages.error = (request, 'خطأ في راس القيد') 
  
      # return redirect('qayd_all')    
    context = {
        'all_qayd': Qayd.objects.all(),
        'qayd_form': QaydForm(),
        'qayd_details_form': QaydDetailsForm(),
        # 'calc':calc,
        # 'qayd_details_form': QaydDetails(),
    }    
    return render(request,'gaccounts/new_qayd.html', context)

def qayd_update(request, id):
  if request.user.is_authenticated and not request.user.is_anonymous:
    qayd_id = Qayd.objects.get(id=id)
    qayd_form = QaydForm(request.POST, request.FILES, instance=qayd_id)
    qayd_id_details = QaydDetails.objects.filter(qaydID=id)
    qayd_details_form = QaydDetailsForm(request.POST, request.FILES, instance=qayd_id)
    if 'btnsave' in request.POST:
      if request.method == 'POST':
        qayd_id.userID = request.user
        qayd_id.dateQayd = request.POST['dateQayd']
        qayd_id.desQayd = request.POST['desQayd']
        # qayd_id.currencyID = request.POST['currencyID']
        qayd_id.attachments = request.POST['attachments']  
        qayd_id.save()
        # qayd_id_details.qaydID = qayd_id
        # # qayd_id_details.accID = request.POST['accID']
        # qayd_id_details.debit = request.POST['debit']
        # qayd_id_details.credit = request.POST['credit']
        # qayd_id_details.desQaydDetails = request.POST['desQaydDetails']
        # qayd_id_details.projectID = request.POST['projectID']
        # qayd_id_details.empID = request.POST['empID']
        # qayd_id_details.save()
        messages.success(request, 'تم تحديث القيد بنجاح')
        return redirect('qayd_all')
      else:
        messages.error(request, 'خطأ في البيانات')   
    qayd_form = QaydForm(instance=qayd_id)
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
        'qayd_id':qayd_id,
        'qayd_form':qayd_form,
        'qayd_id_details':qayd_id_details,
        'qayd_details_form':qayd_details_form,
        'calc':calc,
    }
    return render(request, 'gaccounts/qayd_update.html', context)
  else:
    messages.info(request, 'الرجاء تسجيل الدخول')
    return redirect('signin')
    
def qayd_delete(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
      qayd_id = Qayd.objects.get(id=id)
      if 'btndelete' in request.POST:
        qayd_id.delete()
        messages.info(request, 'تم حذف القيد بنجاح')
        return redirect('qayd_all')
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
    return render(request, 'gaccounts/qayd_delete.html', context)

def qayd_print(request, qayd_id):
    return redirect('qayd_print')