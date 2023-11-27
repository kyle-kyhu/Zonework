from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Evaluation, Subject
from django.urls import reverse_lazy

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    model = Evaluation

    # def get_queryset(self):
    #     return Evaluation.objects.filter(student=self.request.user)

class SubjectListView(ListView):
    template_name = 'subject_list.html'
    model = Subject


class SubjectDetailView(DetailView):
    template_name = 'subject_detail.html'
    model = Evaluation

    def get_success_url(self):
        return reverse_lazy('home')  # Replace 'home' with the correct URL pattern name
    model = Evaluation