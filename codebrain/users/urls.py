from django.urls import path
from .views import LoginUserView, ProfileUserView, RegistrationUserView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', login_required(ProfileUserView.as_view()), name='profile'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
]
