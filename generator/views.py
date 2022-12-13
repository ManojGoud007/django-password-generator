from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    newPass = ''
    lowCase = list('abcdefghijklmnopqrstuvwxyz')
    #if uppercase is checked
    if request.GET.get('uppercase'):
        lowCase.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        lowCase.extend(list('0123456789'))
    if request.GET.get('splcharacters'):
        lowCase.extend(list('!@#$%^&*()'))
    length = int(request.GET.get('length'))
    for i in range(length):
        newPass+=random.choice(lowCase)

    return render(request,'generator/password.html',{'password':newPass})


