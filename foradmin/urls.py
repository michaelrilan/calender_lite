from django.urls import path
from . import views

urlpatterns = [
    path("",views.admin_index, name = "index"),
    path('admin_index.html', views.admin_index, name='admin_index'),
    path('admin_limit.html', views.admin_limit_view, name='admin_limit_view')
]