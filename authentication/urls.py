from django.urls import path
from .views import register_view, login_view

urlpatterns = [
    path('register/', view=register_view, name='register'),
    path('login/', view=login_view, name='login'),
]
