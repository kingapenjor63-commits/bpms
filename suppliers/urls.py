from django.urls import path
from . import views

app_name = 'suppliers'

urlpatterns = [
    path('', views.portal_home, name='portal_home'),
]