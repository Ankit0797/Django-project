from multiprocessing import context
from django.shortcuts import redirect, render

from .models import Employees

# Create your views here.

def home(request):
    return render(request,'home.html')

def CRF(request):
    return render(request,'form1.html')

# def view_all_emp(request):
#     emps=Employees.objects.all()
#     context = {
#         'emps': emps
#     }
#     print(context)
#     return render(request,'view_all_emp.html', context)

# def add_emp(request):
#     return render(request,'add_emp.html')

# def remove_emp(request):
#     return render(request,'remove_emp.html')

# def filter_emp(request):
#     return render(request,'filter_emp.html')