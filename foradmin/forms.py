from socket import fromshare
from django import forms
from .models import *
from .models import admin_limit


class admin_mema_form_admin_limit(forms.ModelForm):
    class Meta:
        model = admin_limit
        fields = '__all__'

class admin_mema_form_admin_date_block(forms.ModelForm):
    class Meta:
        model = admin_date_block
        fields = '__all__'