from django.urls import path
from .views import  home_view, home_authenticated, create_card

urlpatterns = [
    path('', view=home_view, name='home'),
    path('home/', view=home_authenticated, name="homepage"),
    path('create/', view=create_card, name="create_card")
]
