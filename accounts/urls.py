from django.urls import path
from .views import SignUpView, UserListView, UserUpdateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='userlist'),
    path('edituser/<int:pk>/', UserUpdateView.as_view(), name='edituser'),

]