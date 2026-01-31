from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import short_urls
from .utils import base62_encoding
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        orginal_url = request.POST.get("url")

        if not orginal_url:
            messages.error(request, "URL is required")
            return redirect(request,'core/home.html')

        obj = short_urls.objects.create(
            user = request.user,
            orginal_url = orginal_url,
            short_url = 'temp'
        )
        obj.short_url = base62_encoding(obj.id)
        obj.save(update_fields=['short_url'])
        messages.success(request, "Short URL Generated Successfully")
        return redirect('home')
    urls = short_urls.objects.filter(user = request.user).order_by('-created_at')
    return render(request, 'core/home.html', {'short_urls':urls,})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Password didn't Match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')  
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request,"Registration successful, Please Login")
        return redirect('register')
    
    return render(request, 'core/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('login')
    
    return render(request,'core/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_url(request,id):
    queryset = short_urls.objects.get(id=id)
    queryset.delete()
    return redirect('home')