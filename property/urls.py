from django.urls import path
from . import views

urlpatterns = [
   
    path('propertygrid/<int:cat_id>/', views.property, name='properties'),
    path('propertygrid/<int:cat_id>/<int:prod_id>/', views.singleproperty, name='singleproperty'),
    path('propertygrid/<int:cat_id>/<int:prod_id>/orders/', views.orders, name='orders')
]
