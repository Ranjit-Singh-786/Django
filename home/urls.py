from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('service',views.service,name='service'),
    path('varRender',views.varRender,name='varRender'),
    path('formsubmit', views.formsubmit, name='formsubmit'),
    path('input_submit',views.input_submit,name='input_submit')
]
