from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from .models import Evaluation, Subject
from .forms import EvaluationForm
from django.urls import reverse_lazy

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    model = Evaluation

    # def get_queryset(self):
    #     return Evaluation.objects.filter(student=self.request.user)

class SubjectListView(ListView):
    template_name = 'subject_list.html'
    model = Subject

'''this was the first attempt to get the evaluation form to work'''
# class SubjectDetailView(DetailView):
#     template_name = 'subject_detail.html'
#     model = Evaluation

#     def get_success_url(self):
#         return reverse_lazy('home')  # Replace 'home' with the correct URL pattern name
#     model = Evaluation

class EvaluationGet(LoginRequiredMixin, DetailView):
    template_name = 'subject_detail.html'
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EvaluationForm()
        return context
    
class EvaluationPost(SingleObjectMixin, FormView):
    template_name = 'subject_detail.html'
    model = Subject
    form_class = EvaluationForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        # create an instance of the evaluation model, but don't save it yet
        evaluation = form.save(commit=False)
        # set the subject and student for the evaluation
        evaluation.subject = self.object
        evaluation.student = self.request.user

        if form.cleaned_data['understand']:
        # check if the 'understand' buttton was clicked
            evaluation.not_yet = False
        else:
            evaluation.understand = False
        
        evaluation.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('subject_detail', kwargs={'pk': self.object.pk})
        
    def get_success_url(self):
        return reverse_lazy('subject_detail', kwargs={'pk': self.object.pk})

class SubjectDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = EvaluationGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = EvaluationPost.as_view()
        return view(request, *args, **kwargs)