from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer
# Create your views here. 
def sign_out(request):
    logout(request)
    return redirect('home')
def show_account(request):
    context={}
    if request.POST and  'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            # creates user Accounts
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            # create customer Account 
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address,
            )
            sucess_message="User register sucessfully"
            messages.success(request,sucess_message)
        except Exception as e:
            error_message = " Exist Username or Invalid  Username "
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or Password')
    return render (request,'account.html',context)
