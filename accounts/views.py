from django.views.generic import CreateView, ListView, UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect


# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    success_url = reverse_lazy('main')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'edit_user.html'
    fields = ['age', 'alias', 'email', 'username']
    success_url = reverse_lazy('main')

