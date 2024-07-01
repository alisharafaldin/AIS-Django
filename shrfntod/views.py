from django.shortcuts import render
from .models import Posts, Album
# Create your views here.

# def blog(r):
#     all_postes = Posts.objects.all()
#     return render(r,'pages/blog.html',{'all_postes':all_postes})