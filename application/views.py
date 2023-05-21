from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import random
from .otp import sms
from .forms import signupform
from .models import Details,Otp
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password1)
            login(request,user)
            return redirect('details')
    else:
        form = signupform()
    return render(request,'signup.html', {'form' : form}) 

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('display')
            
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def details(request):
    if request.method == 'POST':
        username = request.user.username
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        district = request.POST.get('district')
        city = request.POST.get('city')
        aka = Details(username=username,firstname=firstname,lastname=lastname,email=email,mobile=mobile,address=address,district=district,city=city)
        aka.save()
        logout(request)
        return redirect('home')
    return render(request,'details.html')

@login_required(login_url='login')
def display(request):
    username = request.user.username
    if Details.objects.filter(username=username).exists():
        user_details = Details.objects.filter(username=username).values()
        context = {
            'firstname' : user_details[0]['firstname'],
            'lastname' : user_details[0]['lastname'],
            'email' : user_details[0]['email'],
            'mobile' : user_details[0]['mobile'],
            'address' : user_details[0]['address'],
            'district' : user_details[0]['district'],
            'city' : user_details[0]['city'],
        }
        return render(request,'display.html',context)
    else:
        return redirect('details')
    
@login_required
def forgot(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if Details.objects.filter(username = username).exists():
            details = Details.objects.filter(username=username).values()
            phone = "+91"+ details[0]['mobile']
            otp = random.randint(10000,100000)
            sms(phone,"your otp for password reset is"+str(otp))
            onetime = Otp(username=username,otp=otp)
            onetime.save()
            return render(request,'otp.html')

    return render(request,'forgot.html')

