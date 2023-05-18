from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .forms import signupform
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
            login(request, user)
            return redirect('home')
    else:
        form = signupform()
    return render(request,'signup.html', {'form' : form}) 