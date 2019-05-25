
from django.views.generic import TemplateView, ListView,  DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tool
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Tool


class MainUserListView(LoginRequiredMixin, ListView):
    template_name = 'main.html'
    model = Tool


class MyToolsListView(ListView):
    model = Tool
    template_name = 'my_tool.html'
    success_url = reverse_lazy('main')

    def get_queryset(self):
        return Tool.objects.filter(owner=self.request.user)


class ToolDetailView(DetailView):
    template_name = 'tools_detail.html'
    model = Tool


class ToolCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tool_create.html'
    model = Tool
    fields = ['owner', 'toolname', 'type_of_tool', 'description', 'model_pic', 'location']
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EachUsersToolsLIstView(ListView):
    template_name = 'each_users_tool.html'
    model = Tool

    def get_queryset(self):
        return Tool.objects.filter(owner__id=self.kwargs['pk'])


class EditToolView(UpdateView):
    template_name = 'edit_tool.html'
    model = Tool
    fields = ['owner', 'toolname', 'type_of_tool', 'description', 'model_pic', 'location']
    success_url = reverse_lazy('my_tool')


class DeleteToolView(DeleteView):
    model = Tool
    template_name = 'delete_tool.html'
    success_url = reverse_lazy('main')

# class ToolBelongsToUser(LoginRequiredMixin, ListView)
