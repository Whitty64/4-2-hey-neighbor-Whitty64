from django.urls import path
from .views import HomePageView, MainUserListView, ToolDetailView, ToolCreateView, MyToolsLIstView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('main/', MainUserListView.as_view(), name='main'),
    path('tool/<int:pk>/', ToolDetailView.as_view(), name='tools_detail'),
    path('tool/new/', ToolCreateView.as_view(), name='tool_new'),
    path('tool/mytools/<int:pk>/', MyToolsLIstView.as_view(), name='my_tool'),

]