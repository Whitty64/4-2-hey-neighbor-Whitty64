
from django.views.generic import TemplateView, ListView,  DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tool
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Tool


class MainUserListView(ListView):
    template_name = 'main.html'
    model = Tool


class MyToolsLIstView(ListView):
    template_name = 'my_tool.html'
    model = Tool

    def get_queryset(self):
        return Tool.objects.filter(owner=self.kwargs['pk'])


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

# class ToolBelongsToUser(LoginRequiredMixin, ListView)
