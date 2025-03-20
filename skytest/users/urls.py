from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import SkyAuthenticationForm
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=SkyAuthenticationForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
