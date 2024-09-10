from django.shortcuts import render, redirect
from authentication.models import List
from .forms import CardForm
from django.contrib import messages

def home_view(request):
  return render(request, 'index.html')

def home_authenticated(request):
    form = CardForm()
    listing = List.objects.all()
    context = {
        'list': listing,
        'form': form
    }
    return render(request, 'home.html', context=context)

def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card created successfully.')
        else:
            print(form.errors)
            messages.error(request, 'There was an error creating the card.')
    return redirect('homepage')
