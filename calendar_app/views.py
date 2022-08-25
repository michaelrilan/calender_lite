from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date, timedelta
import datetime
from django.contrib import messages
from .models import *
from .forms import *
def index(request):
    form = mema_form()
    if request.method == 'POST':
        form = mema_form(request.POST)
        first_name= form['first_name'].value()
        last_name= form['last_name'].value()
    

        if form.is_valid():
        #if User.objects.filter(username=uservalue).exists():
            form.save()
            messages.success(request, "Successfully Registered")
    context = {'form': form}
    return render(request, "index.html",context)

