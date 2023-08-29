
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

def new_qayd(request):
  if request.method == 'POST':
    debit  = request.POST['debit']
    credit = request.POST['credit']
    desQaydDetails = request.POST['desQaydDetails']
    accID = request.POST['accID']
    projectID = request.POST['projectID']
    empID = request.POST['empID']
    if 'debit' in request.POST: debit = request.POST['debit']
    else: messages.error(request, 'Error in debit')
    if 'credit' in request.POST: credit = request.POST['credit']
    else: messages.error(request, 'Error in credit')
    if 'desQaydDetails' in request.POST: desQaydDetails = request.POST['desQaydDetails']
    else: messages.error(request, 'Error in desQaydDetails')
    if 'accID' in request.POST: accID = request.POST['accID']
    else: messages.error(request, 'Error in accID')
    if 'projectID' in request.POST: projectID = request.POST['projectID']
    else: messages.error(request, 'Error in ')
    if 'empID' in request.POST: empID = request.POST['empID']
    else: messages.error(request, 'Error in empID')
    newqayd = QaydForm(request.POST, request.FILES)
    if newqayd.is_valid():
      newqayd.save()
      newqayd_d = QaydDetails(qaydID=newqayd.instance, debit=debit, credit=credit, desQaydDetails=desQaydDetails, accID_id=accID, projectID_id=projectID, empID_id=empID)
      newqayd_d.save()
      messages.success(request, 'تمت الإضافة بنجاح') 
      return redirect('qayds')
    else :      
      messages.error(request, 'خطأ في البيانات') 
  context = {
      'all_qayd': Qayd.objects.all(),
      'qayd_form': QaydForm(),
      'qayd_details_form': QaydDetailsForm(),
  }    
  return render(request,'gaccounts/new_qayd.html', context)

def view_qayd(request, qayd_id):
    return redirect('qayd_print')

def update_qayd(request, id):
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
        qayd_id.currencyID_id = request.POST['currencyID']
        qayd_id.attachments = request.POST['attachments']  
        qayd_id.save()
        # qayd_id_details.qaydID = qayd_id
        # qayd_id_details.accID = request.POST['accID']
        # qayd_id_details.debit = request.POST['debit']
        # qayd_id_details.credit = request.POST['credit']
        # qayd_id_details.desQaydDetails = request.POST['desQaydDetails']
        # qayd_id_details.projectID = request.POST['projectID']
        # qayd_id_details.empID = request.POST['empID']
        # qayd_id_details.save()
        messages.success(request, 'تم تحديث القيد بنجاح')
        return redirect('qayds')
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
    return render(request, 'gaccounts/update_qayd.html', context)
  else:
    messages.info(request, 'الرجاء تسجيل الدخول')
    return redirect('signin')
    
def delete_qayd(request, id):
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
    return render(request, 'gaccounts/delete_qayd.html', context)

def qayds(request):    
    context = {
        'all_qayd':Qayd.objects.all(),
    }
    return render(request,'gaccounts/qayds.html', context)
