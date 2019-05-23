from django.urls import path
from .views import SignUpView, UserListView, LoginView, UserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='userlist'),
    path('edituser/<int:pk>/', UserUpdateView.as_view(), name='edituser')

]