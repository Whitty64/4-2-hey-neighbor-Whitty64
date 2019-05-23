from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('main')


class LoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'


class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    success_url = reverse_lazy('main')


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'edit_user.html'
    success_url = reverse_lazy('main')
    fields = ['age', 'alias']
