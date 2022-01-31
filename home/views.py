from django.shortcuts import render
from property.models import Category 

# Create your views here.
def home(request):
    cat = Category.objects.all()
    return render(request,'index.html', {'cats' : cat})

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signuplogin.html')
