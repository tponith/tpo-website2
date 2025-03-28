"""training and placement portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from . import views

urlpatterns = [
    #home page
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^contact/', views.contact, name='contact'),
    re_path(r'^facilities/', views.facilities, name='facilities'),
    re_path(r'^invitation/', views.invitation, name='invitation'),
    re_path(r'^how-to-reach/', views.reach, name='reach'),
    re_path(r'^functionaries/', views.functionaries, name='functionaries'),
    re_path(r'^student-functionaries/', views.student_functionaries, name='student_functionaries'),
    re_path(r'^directors-desk/', views.director, name='director'),
    re_path(r'^registrar/', views.registrar, name='registrar'),
    re_path(r'^training-Placement-Office/', views.office, name='office'),
    re_path(r'^placement-procedure/', views.placement, name='placement'),
    re_path(r'^placement-record/', views.record, name='record'),
    re_path(r'^past-recruiters/', views.recruiters, name='recruiters'),
    re_path(r'^internship-procedure/', views.internship, name='internship'),
    re_path(r'^training-internship-opportunities/', views.opportunities, name='opportunities'),
]
