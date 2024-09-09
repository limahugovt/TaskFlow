from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import LoginForm, RegisterForm
from .models import User, Card

def register_view(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      password = form.cleaned_data['password']
      password_confirm = form.cleaned_data['password_confirm']
      if password != password_confirm:
        return render(request, 'register.html', {'form': form, 'error': 'Passwords do not match'})
      else:
        User.objects.create_user(
          name=form.cleaned_data['name'],
          email=form.cleaned_data['email'],
          password=form.cleaned_data['password']
        )
        return redirect('login')
  else:
    form = RegisterForm()
  return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
  return render(request, 'index.html')

def home_authenticated(request):
   card = Card.objects.all()
   print(card)
   context = {
      'card': card
   }
   return render(request, 'home.html', context=context)
