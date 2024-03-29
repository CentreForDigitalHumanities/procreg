
from django.contrib.auth import views as auth_views
from django.urls import path

from registrations.views import LandingView

app_name = 'main'

urlpatterns = [
    path('', LandingView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
