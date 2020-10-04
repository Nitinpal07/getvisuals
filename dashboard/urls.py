from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path('report/retail', views.ecommerce_report_page, name='retail_report'),
    path('report/marketing', views.marketing_report_page, name='marketing_report'),
    path('report/about', views.about_page, name='about'),
]

