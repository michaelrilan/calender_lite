from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.


def admin_index(request):
    form = admin_mema_form_admin_date_block()
    if request.method == 'POST':
        form = admin_mema_form_admin_date_block(request.POST)
        date_blockk= form['date_block'].value()
        if form.is_valid():
            admin_date_block.objects.filter(pk=1).update(date_block=date_blockk)
            messages.success(request, "Successfully Saved")

            
    context = {'form': form
    }

    return render(request, "admin_index.html",context)

def admin_limit_view(request):
    form = admin_mema_form_admin_limit()
    date_blockget = admin_limit.objects.values_list('entry_limit', flat=True).get(pk=1)
    if request.method == 'POST':
        form = admin_mema_form_admin_limit(request.POST)
        entry_limitt = form['entry_limit'].value()
        if form.is_valid():
            admin_limit.objects.filter(pk=1).update(entry_limit=entry_limitt)
            messages.success(request, "Successfully Saved")


    context = {}
    return render(request, "admin_limit.html", context)
