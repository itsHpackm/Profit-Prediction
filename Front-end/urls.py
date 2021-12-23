from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('getForm', views.getForm, name='getForm'),

]
