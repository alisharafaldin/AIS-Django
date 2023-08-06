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

def qayd_update(request, id):
    # details_formset = modelform_factory(QaydDetails, fields=('qaydID',))
    # formset = details_formset(queryset=QaydDetails.objects.filter(details_formset__id=QaydDetails.id))
  if request.user.is_authenticated and not request.user.is_anonymous:
    qayd_id = Qayd.objects.get(id=id)
    qayd_id_details = QaydDetails.objects.all().filter(qaydID=qayd_id)
    if request.method == 'POST' and 'btnsave' in request.POST:
      qayd_form = QaydForm(request.POST, request.FILES, instance=qayd_id)
      if qayd_form.is_valid():
         qayd_form.save()
        #  qayd_details_form = QaydDetailsForm(request.POST, instance=qayd_id)
        #  if qayd_details_form.is_valid():
        #     qayd_id_details.save()
         messages.success(request, 'تم تحديث القيد بنجاح')
         return redirect('qayd_all')
      else:
        messages.error(request, 'خطأ في البيانات')   
    qayd_form = QaydForm(instance=qayd_id)
    qayd_details_form = QaydDetailsForm(instance=qayd_id)
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
    qayd_id_details = QaydDetails.objects.all().filter(qaydID=id)
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

# def test(request):
#     return HttpResponse(request.POST[''])

# def qayd_add(request):
    # new_qayd = Qayd()
    # if request.method == 'POST' and 'btnsave' in request.POST:
      # new_qayd.userID = request.POST['userID']
      # new_qayd.dateQayd = request.POST['dateQayd']
      # new_qayd.desQayd = request.POST['desQayd']
      # new_qayd.currencyID = request.POST['currencyID']
      # new_qayd.attachments = request.POST['attachments']
      # new_qayd.save()
      # print(request.POST['currencyID'])
      # debit = request.POST['debit']
      # credit = request.POST['credit']
      # desQaydDetails = request.POST['desQaydDetails']
      # accID = request.POST['accID']
      # projectID = request.POST['projectID']
      # empID = request.POST['empID']
      # qayddetails = QaydDetails.objects.create(qaydID=new_qayd, debit=debit, credit=credit, desQaydDetails=desQaydDetails, accID=accID, projectID=projectID, empID=empID )
      # qayddetails.save()
      # messages.success(request, 'تمت إضافة القيد بنجاح')
      # return redirect('qayd_all')   
    # else:
      # messages.error = (request, 'خطأ في حفظ القيد')
    # context = {
        # 'all_qayd': Qayd.objects.all(),
        # 'qayd_form': QaydForm(),
        # 'qayd_details_form': QaydDetailsForm(),
    # }    
    # return render(request,'gaccounts/qayd_add.html', context)


# def qayd_update(request, id):
#     if request.user.is_authenticated and not request.user.is_anonymous:
#       qayd_update = Qayd.objects.get(id=id)
#       qayd_details_update = QaydDetails.objects.all().filter(qaydID=qayd_update)
#       qayd_form = QaydForm(instance=qayd_update)
#       # qayd_details_form = QaydDetailsForm(initial=3)
#       qayd_details_form = QaydDetailsForm(instance=qayd_details_update)
#       if  'btnsave' in request.POST:
#         if request.method == 'POST':
#             # qayd_update.userID = request.POST['userID']
#             qayd_update.dateQayd = request.POST['dateQayd']
#             qayd_update.desQayd = request.POST['desQayd']
#             qayd_update.currencyID = request.POST['currencyID']
#             qayd_update.attachments = request.POST['attachments']
#             qayd_update.save()
#             messages.success(request, 'تمت تحديث القيد بنجاح')  
#             return redirect('qayd_all')   
#         else:
#             messages.error(request, 'خطأ في إستقبال البيانات')  
#       context = {
#           'qayd_form':qayd_form,
#           'qayd_details_form': qayd_details_form,
#           'qayd_update':qayd_details_update,
#       }
#       return render(request, 'gaccounts/qayd_update.html', context)
#     else:
#         messages.info(request, 'الرجاء تسجيل الدخول' )
#         return redirect('qayd_all')    

