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

def create_learning_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            learning_item = form.save(commit=False)
            learning_item.student = request.user.student
            learning_item.save()
    return redirect("learning")


def update_completed(request, item_id):
    learning_item = LearningItem.objects.get(id=item_id)
    if request.method == "POST":
        completed_value = request.POST.get("completed")
        if completed_value == "ok":
            learning_item.completed = True
        elif completed_value == "nok":
            learning_item.completed = False
        learning_item.save()
    return redirect("learning")


class DashboardPageView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ongoing_count'] = LearningItem.objects.filter(completed=False).count()
        context['finalized_count'] = LearningItem.objects.filter(completed=True).count()
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"
