from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import UserLoginForm, ProfileUserForm, UserRegistrationForm
from .models import User


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class ProfileUserView(UpdateView):
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class RegistrationUserView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse_lazy('profile')
