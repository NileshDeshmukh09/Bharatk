from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'),
    path('contact', views.contact, name='contact'),
]
