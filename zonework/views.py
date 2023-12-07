from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from .models import Evaluation, Subject
from .forms import EvaluationForm
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.db.models.functions import ExtractWeekDay
from django.utils import timezone
from datetime import timedelta, datetime, time

class SubjectListView(ListView):
    template_name = 'subject_list.html'
    model = Subject

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
    

class SubjectRecapView(LoginRequiredMixin, TemplateView):
    """This view is a mini recap of the evaluations"""
    template_name = 'subject_detail.html'
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['understand_count'] = Subject.objects.filter(understand=True).count()
        context['not_yet_count'] = Subject.objects.filter(not_yet=True).count()
        context['both_count'] = Subject.objects.filter(Q(understand=True) & Q(not_yet=True)).count()

        # Get the current date
        today = timezone.now().date()

        # Get the datetime for the start and end of today
        start_of_today = timezone.make_aware(datetime.combine(today, time.min))
        end_of_today = timezone.make_aware(datetime.combine(today, time.max))

        # Count 'both_count' within today's calendar day
        context['both_count_today'] = Subject.objects.filter(
            Q(understand=True) & Q(not_yet=True) & Q(created_at__range=(start_of_today, end_of_today))
        ).count()

        # Count the evaluations for each day of the week
        evaluations_per_day = Subject.objects.annotate(
            day_of_week=ExtractWeekDay('created_at')
        ).values('day_of_week').annotate(count=Count('id')).order_by('day_of_week')

        context['evaluations_per_day'] = {
            'Monday': 0,
            'Tuesday': 0,
            'Wednesday': 0,
            'Thursday': 0,
            'Friday': 0,
            'Saturday': 0,
            'Sunday': 0,
        }

        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        for item in evaluations_per_day:
            context['evaluations_per_day'][days_of_week[item['day_of_week'] - 1]] = item['count']

        return context

    
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    model = Subject