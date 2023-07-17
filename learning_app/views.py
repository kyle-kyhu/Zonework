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


#class LearningPageView(CreateView):
#    model = LearningItem
#    template_name = "learning.html"
#    fields = ["completed", "text"]
#    context_object_name = "list_of_items"
#    success_url = reverse_lazy("learning")

class LearningPageView2(CreateView):
    model = LearningItem
    template_name = "learning.html"
    form_class = ItemForm
    success_url = reverse_lazy("learning")

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        return super().form_valid(form)

    def get_queryset(self):
        return LearningItem.objects.filter(student=self.request.user.student)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["queryset"] = self.get_queryset()
        context["list_of_items"] = LearningItem.objects.filter(student=self.request.user.student)
        return context 



class DashboardPageView(ListView):
    model = LearningItem
    template_name = "dashboard.html"
    context_object_name = "list_of_items"


class AboutPageView(TemplateView):
    template_name = "about.html"
