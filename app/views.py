from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def display_dept(request):
    dol=Dept.objects.all()
    dol=Dept.objects.filter(Dept_no='20')
    dol=Dept.objects.filter(Dname__startswith='s')
    dol=Dept.objects.all()
    dol=Dept.objects.filter(Dname__endswith='s')
    dol=Dept.objects.filter(Dname__contains='o')
    dol=Dept.objects.all()
    #dol=Dept.objects.filter(Dname__in=('sales','research'))
    d={'dept':dol}
    return render(request,'display_dept.html',d)
def display_emp(request):
    eol=Emp.objects.all()
    eol=Emp.objects.filter(Hire_date__year='1981')
    eol=Emp.objects.filter(Hire_date__month__gt='9')
    eol=Emp.objects.filter(Hire_date__year__in=('1981','1980'))
    eol=Emp.objects.filter(Q(Ename='SMITH') & Q(Sal='800'))
    eol=Emp.objects.all().order_by('Ename')
    eol=Emp.objects.all()[0:5]
    
    eol=Emp.objects.all()
    E={'emp':eol}
    return render(request,'display_emp.html',E)