from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date, timedelta
import datetime

def index(response):
    return HttpResponse("<p>pukininam</p>")