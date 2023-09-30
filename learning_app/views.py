from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

# from .forms import SessionForm
from .models import Student, Subject, Session


class HomePageView(TemplateView):
    template_name = "home.html"


class SubjectPageView(CreateView):
    model = Subject
    template_name = "subject.html"
    fields = ["enter_subject"]
    success_url = reverse_lazy("session")


# class SessionPageView(View):  # this might require loginrequiredmixin
#     def get(self, request, *args, **kwargs):
#         view = SessionPageView.as_view()
#         return view(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         view = SessionPageView.as_view()
#         return view(request, *args, **kwargs)


"""Commented out old code below"""


class SessionPageView(CreateView, ListView):
    model = Session
    template_name = "session.html"
    # form_class = SessionForm
    fields = ["assessment", "assessment_description"]
    context_object_name = "list_of_session_items"
    success_url = reverse_lazy("session")


""" Remove this fields in order to debug IntegrityError at /session/..NOT NULL constraint failed:"""

# def post(self, request, *args, **kwargs):
#     self.object - self.get_object()
#     return super().post(request, *args, **kwargs)

# def form_valid(self, form):
#     session = form.save(commit=False)
#     session.subject = self.get_object
#     session.student = self.request.user
#     session.save()
#     return super().form_valid(form)


class DashboardPageView(ListView):
    model = Session
    template_name = "dashboard.html"
    context_object_name = "list_of_session_items"


class AboutPageView(TemplateView):
    template_name = "about.html"
