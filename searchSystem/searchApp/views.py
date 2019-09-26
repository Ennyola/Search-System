from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def login_page(request):
    return render(request, "index.html")

def init_login(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect("searchapp:search")
    else:
        messages.error(request, "Invalid Login Credentials")
        return redirect("searchapp:login")



def search_bar(request):
    fullname = request.POST.get("fullname", None)
    school = request.POST.get("school", None)
    grad_year = request.POST.get("grad_year" , None)

    if fullname and school and grad_year:
        student = Student.objects.filter(Q(fullname = fullname) & Q(school__name = school) & Q(year_of_grad = grad_year))
        context = {"student":student}
    elif fullname and school:
        student = Student.objects.filter(Q(fullname = fullname) & Q(school__name = school))
        context = {"student":student}
    elif fullname and grad_year:
        student = Student.objects.filter(Q(fullname = fullname) & Q(year_of_grad = grad_year))
        context = {"student":student}
    elif school and grad_year:
        student = Student.objects.filter(Q(school__name = school) & Q(year_of_grad = grad_year))
        context = {"student":student}
    elif fullname:
        student = Student.objects.filter(Q(fullname = fullname))
        context = {"student":student}
    elif school:
        student = Student.objects.filter(Q(school__name = school))
        context = {"student":student}
    elif grad_year:
        student = Student.objects.filter(Q(year_of_grad = grad_year))
        context = {"student":student}
    else:
        student = ""
        context = {"student":student}
    
    return render(request, "searchbar.html", context)

def logout_view(request):
    logout(request)
    return redirect("searchapp:sign-in")
