# -*- coding: utf-8 -*-


from django.urls import path

from . import views

app_name = 'pdfanalyzer'
urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('analyse/', views.analyse, name='analyse'),
]
