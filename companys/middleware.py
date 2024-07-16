from .models import Company

# إضافة وسيط لتحديد الشركة الحالية من الجلسة

class CurrentCompanyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            company_id = request.session.get('current_company_id')
            if company_id:
                try:
                    # تحقق مما إذا كان المستخدم جزءًا من الشركة سواء كان مالكًا أو مستخدمًا عاديًا
                    request.current_company = Company.objects.filter(id=company_id, companys__userID=request.user
                    ).distinct().first()
                except Company.DoesNotExist:
                    request.current_company = None
            else:
                request.current_company = None
        else:
            request.current_company = None

        response = self.get_response(request)
        return response
