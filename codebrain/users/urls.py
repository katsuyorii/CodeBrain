from django.urls import path
from .views import LoginUserView, ProfileUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
]
