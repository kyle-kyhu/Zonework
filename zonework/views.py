from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Subject, Evaluation
from .forms import AssessmentForm, EvaluationForm


class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = "subject_list.html"


# class AssessmentGet(LoginRequiredMixin, DetailView):
#     model = Subject
#     template_name = "subject_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = AssessmentForm()
#         return context


# class AssessmentPost(SingleObjectMixin, FormView):
#     model = Subject
#     form_class = AssessmentForm
#     template_name = "subject_detail.html"

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().post(request, *args, **kwargs)

#     def form_valid(self, form):
#         assessment = form.save(commit=False)
#         assessment.subject = self.object
#         assessment.student = self.request.user
#         assessment.save()
#         return super().form_valid(form)

#     def get_success_url(self):
#         subject = self.object
#         return reverse("subject_detail", kwargs={"pk": subject.pk})  
    
class EvaluationGet(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = "subject_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EvaluationForm()
        return context


class EvaluationPost(SingleObjectMixin, FormView):
    model = Subject
    form_class = EvaluationForm
    template_name = "subject_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Create an instance of the Evaluation model, but don't save it to the database yet
        assessment = form.save(commit=False)

        # Set the subject and student for the evaluation
        assessment.subject = self.object
        assessment.student = self.request.user

        # Check if 'understand' is selected and set 'not_yet' accordingly
        if form.cleaned_data['understand']:
            assessment.not_yet = False
        else:
            assessment.understand = False

        # Save the evaluation to the database
        assessment.save()

        return super().form_valid(form)

    def get_success_url(self):
        subject = self.object
        return reverse("subject_detail", kwargs={"pk": subject.pk})


    def get_success_url(self):
        subject = self.object
        return reverse("subject_detail", kwargs={"pk": subject.pk})  


class SubjectDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = EvaluationGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = EvaluationPost.as_view()
        return view(request, *args, **kwargs)


class SubjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subject
    fields = {
        "title",
    }
    template_name = "subject_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.student == self.request.user


class SubjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject
    template_name = "subject_delete.html"
    success_url = reverse_lazy("subject_list")

    def test_func(self):
        obj = self.get_object()
        return obj.student == self.request.user


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    template_name = "subject_new.html"
    fields = ["title"]

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
