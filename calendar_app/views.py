from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date, timedelta
import datetime
from django.contrib import messages
from .models import *
from foradmin.models import admin_date_block,admin_limit
from .forms import *
from datetime import datetime
def index(request):
    form = mema_form()
    entry_limit = admin_limit.objects.values_list('entry_limit', flat=True).get(pk=1)
    date_blockzxc = admin_date_block.objects.values_list('date_block', flat=True).get(pk=1)
    date_time_obj = datetime.strptime(date_blockzxc, "%m/%d/%Y").date()
    date_time_obj_porma = date_time_obj.strftime("%m/%d/%Y")
    petsa_ngayon = datetime.today().strftime("%m/%d/%Y")
    cnt = limit.objects.all().count()
    print(petsa_ngayon)
    print(date_time_obj_porma)
    print(cnt)
    print(entry_limit)
    statee = ""
    if request.method == 'POST':
        form = mema_form(request.POST)
        if form.is_valid() and cnt<entry_limit and petsa_ngayon != date_time_obj_porma:
            form.save()
            messages.success(request, "Successfully Registered")
        else:
            statee = "exceeded"
            messages.info(request, "Form_expired")
    context = {'form': form,
    "statee": statee
    }
    return render(request, "index.html",context)

