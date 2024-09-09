from django.urls import path
from .views import register_view, login_view, home_view, home_authenticated

urlpatterns = [
    path('register/', view=register_view, name='register'),
    path('login/', view=login_view, name='login'),
    path('', view=home_view, name='home'),
    path('home/', view=home_authenticated, name="homepage"),
]
