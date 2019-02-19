"""This is the Url for base"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lipa import views

urlpatterns = [
    path('', views.LipaMpesa.as_view(), name='lipa'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
