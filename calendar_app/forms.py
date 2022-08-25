from socket import fromshare
from django import forms
from .models import *
from .models import limit

class mema_form(forms.ModelForm):
    class Meta:
        model = limit
        fields = '__all__'