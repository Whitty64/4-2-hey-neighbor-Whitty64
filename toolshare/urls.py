from django.urls import path
from .views import MainUserListView, ToolDetailView, ToolCreateView, MyToolsListView,\
    EachUsersToolsLIstView, EditToolView, DeleteToolView

from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('main/', MainUserListView.as_view(), name='main'),
    path('tool/<int:pk>/', ToolDetailView.as_view(), name='tools_detail'),
    path('tool/new/', ToolCreateView.as_view(), name='tool_new'),
    path('tool/mytool/<int:pk>/', MyToolsListView.as_view(), name='my_tools'),
    path('tool/eachusertool/<int:pk>/', EachUsersToolsLIstView.as_view(), name='each_tool'),
    path('tool/edit/<int:pk>', EditToolView.as_view(), name='edit_tool'),
    path('tool/delete/<int:pk>', DeleteToolView.as_view(), name='delete_tool'),

]