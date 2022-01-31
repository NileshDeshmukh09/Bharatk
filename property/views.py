from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from property.models import Property  , Category, Order

# Create your views here.
def property(request,cat_id):
    products = Property.objects.filter(category=cat_id)
    print("Hello")
    return render(request, 'propertygrid.html', {'products':products})


def singleproperty(request, prod_id, cat_id):
    product = Property.objects.get(id=prod_id)
    # product_images = ProductImages.objects.filter(product_id=prod_id)
    return render(request, 'propertysingle.html',{"products":product})


def orders(request, prod_id, cat_id):
    order = Order()
    order.product = Property.objects.get(id=prod_id)
    order.user = request.user
    order.save()
    
    return redirect("/")
