from django.shortcuts import render
from authentication.models import List

def home_view(request):
  return render(request, 'index.html')

def home_authenticated(request):
  listing = List.objects.all()
  context = {
    'list': listing
  }
  return render(request, 'home.html', context=context)
