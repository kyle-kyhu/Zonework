from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Student, LearningItem
from .forms import ItemForm


class HomePageView(TemplateView):
    template_name = "home.html"


class SubjectPageView(CreateView):
    model = LearningItem
    template_name = "subject.html"
    fields = ["subject"]
    success_url = reverse_lazy("learning")


class LearningPageView(CreateView, ListView):
    model = LearningItem
    template_name = "learning.html"
    fields = ["completed", "text"]
    context_object_name = "list_of_items"
    success_url = reverse_lazy("learning")


class DashboardPageView(ListView):
    model = LearningItem
    template_name = "dashboard.html"
    context_object_name = "list_of_items"


class AboutPageView(TemplateView):
    template_name = "about.html"
