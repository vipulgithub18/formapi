from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def ShowFormData(request):
    fm = StudentRegistration()
    return render(request,'enroll/registration.html',{'form':fm})

def home(request):
    nm = 'vipul patil'
    return render(request,'enroll/home.html',{'name':nm})