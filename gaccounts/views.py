from django.shortcuts import render , redirect
from django.contrib import messages
from django.views.generic import CreateView
from . models import AccountsTree , Qayd ,QaydDetails
from employees.models import EmpInfo
from . forms import AccountsTreeForm, QaydForm, QaydDetailsForm
from django.utils import timezone

# Create your views here.

def acc_all(request):
    context = {
        'acc_all':AccountsTree.objects.all(),
    }
    return render(request,'gaccounts/acc_all.html', context)

def acc_add(request):
    if request.method == 'POST':
        add_acc = AccountsTreeForm(request.POST, request.FILES)
        if add_acc.is_valid():
            add_acc.save()
            messages.success(request, 'تمت الإضافة بنجاح') 
    conext = {
        'acc_form': AccountsTreeForm(),
    }    
    return render(request, 'gaccounts/acc_all.html', conext)

def acc_update(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        acc_id = AccountsTree.objects.get(id=id)
        if request.method == 'POST':
            acc_save = AccountsTreeForm(request.POST, request.FILES, instance=acc_id)
            if acc_save.is_valid():
                acc_save.save()
                messages.success(request, 'تمت تحديث البيانات بنجاح')       
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

    # debit = request.POST['debit']
    # credit = request.POST['credit']
    # desQaydDetails = request.POST['desQaydDetails']
    # accID = request.POST['accID']
    # projectID = request.POST['projectID']
    # empID = request.POST['empID']

    if request.method == 'POST':
        new_qayd = QaydForm(request.POST, request.FILES)
        if new_qayd.is_valid():
            new_qayd.save()
            # qayddetails = QaydDetails.objects.create(qaydID=new_qayd, debit=debit, credit=credit, desQaydDetails=desQaydDetails, accID=accID, projectID=projectID, empID=empID )
            messages.success(request, 'تمت الإضافة بنجاح')
            # if new_qayd.save():
    all_qayd = Qayd.objects.all()
    context = {
        'all_qayd': all_qayd,
        'qayd_form': QaydForm(),
        'qd_form': QaydDetailsForm(),
    }    
    return render(request,'gaccounts/qayd_add.html', context)

def qayd_update(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        qayd_id = Qayd.objects.get(id=id)
        if request.method == 'POST':
            qayd_save = QaydForm(request.POST, request.FILES, instance=qayd_id)
            if qayd_save.is_valid():
                qayd_save.save()
                messages.success(request, 'تمت تحديث القيد بنجاح')  
                return redirect('qayd_all')   
            else:
                messages.error(request, 'خطأ في البيانات')  
        else:
            qayd_save = QaydForm(instance=qayd_id)
        context = {
            'qayd_form':qayd_save,
        }
        return render(request, 'gaccounts/qayd_update.html', context)
    else:
        messages.info(request, 'الرجاء تسجيل الدخول' )
        return redirect('qayd_all')
    
def qayd_print(request, qayd_id):
    return redirect('qayd_print')