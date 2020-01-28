from django.shortcuts import render,redirect
from app1.forms import EmployeeForm
from app1.models import EmployeeModel
from django.contrib import messages

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def register_page(request):
    ef = EmployeeForm()
    return render(request,"register.html",{"form" : ef})


def save(request):
    na = request.POST.get("name")
    age = request.POST.get("age")
    cno = request.POST.get("contact_no")
    email = request.POST.get("email")
    p1 = request.POST.get("password")
    p2 = request.POST.get("re_password")
    if p1==p2:
        EmployeeModel(name=na,age=age,contact_no=cno,email=email,password=p1).save()
        messages.success(request,"Hurrahh!!! Details are saved succesfully.")
        return redirect('index')
    else:
        messages.error(request,"OOPS!! Password dosen't match ,Try again.")
        return redirect("register_page")
