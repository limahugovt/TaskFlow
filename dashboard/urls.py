from django.urls import path
from .views import  home_view, home_authenticated

urlpatterns = [
    path('', view=home_view, name='home'),
    path('home/', view=home_authenticated, name="homepage"),
]
