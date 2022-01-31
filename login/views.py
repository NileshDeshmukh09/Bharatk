from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Contact
from django.contrib import messages 
# Create your views here.
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
       
        if password == password1:

            user = User.objects.create_user(username=username, password = password, email = email)
            user.save()

            mobile_num = request.POST.get('contact')
            extended_user = Contact(user=user, mobile_num=mobile_num)
            extended_user.save()
            return redirect('login')
        
        else:
            messages.info(request,'Password Did not matched..!!')
            return redirect('register')

    else:
        return render(request, 'signuplogin.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("login")


    else:
        return render(request, 'signuplogin.html')


def logout(request):
    auth.logout(request)
    return redirect("/")