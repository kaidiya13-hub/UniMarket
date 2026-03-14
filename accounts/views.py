from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        cp = request.POST.get('confirm_password')
        
        if p != cp:
            messages.error(request, "Passwords do not match!")
            return render(request, 'accounts/register.html')
        
        # Backend validation: Ensure email has a .edu suffix
        if not e.lower().endswith('.edu'):
            messages.error(request, "A valid university email (.edu) is required.")
            return render(request, 'accounts/register.html')
            
        if not User.objects.filter(username=u).exists():
            User.objects.create_user(username=u, email=e, password=p)
            return redirect('login')
        else:
            messages.error(request, "Username already exists!")
            
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('marketplace')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def profile_view(request):
    return render(request, 'accounts/profile.html')