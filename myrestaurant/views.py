from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Menu
from .forms import CustomAuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    appetizers = Menu.objects.filter(category='Appetizers')
    main_courses = Menu.objects.filter(category='Main Courses')
    desserts = Menu.objects.filter(category='Desserts')
    return render(request, 'index.html', {
        "appetizers": appetizers,
        "main_courses": main_courses,
        "desserts": desserts,
    })

# @login_required
def add_dish(request):
    appetizers = Menu.objects.filter(category='Appetizers')
    main_courses = Menu.objects.filter(category='Main Courses')
    desserts = Menu.objects.filter(category='Desserts')

    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('description')
        p = request.POST.get('price')
        c = request.POST.get('category')
        if n and d and p and c:
            menu = Menu(name=n, description=d, price=p, category=c)
            menu.save()
    
    return render(request, 'add_dish.html', {
        "appetizers": appetizers,
        "main_courses": main_courses,
        "desserts": desserts
    })

def new_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_dish')  # Redirect to a home page or dashboard
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'index.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('login')
    
    return render(request, 'register.html')
