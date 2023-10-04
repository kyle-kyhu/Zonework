from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = "subject_list.html"


class SubjectDetailView(DetailView):
    model = Subject
    template_name = "subject_detail.html"


class SubjectUpdateView(UpdateView):
    model = Subject
    fields = {
        "title",
    }
    template_name = "subject_edit.html"


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "subject_delete.html"
    success_url = reverse_lazy("subject_list")

class SubjectCreateView(CreateView):
    model = Subject
    template_name = "subject_new.html"
    fields = [
        "title",
        "student",
    ]
