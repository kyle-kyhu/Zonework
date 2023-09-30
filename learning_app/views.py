from django.views.generic import ListView, CreateView
from .models import Session


class SummaryListView(ListView):
    model = Session
    template_name = "summary.html"

class SubjectCreateView(CreateView):
    model = Session
    template = "subject.html"
    fields = ["subject"]

class HomeListView(ListView):
    model = Session
    template_name = "home.html"
