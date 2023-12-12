from datetime import datetime, time, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from .models import Evaluation, Subject
from .forms import EvaluationForm
from django.urls import reverse_lazy
from django.db.models import Q, Count, Sum
from django.db.models.functions import ExtractWeekDay
from django.utils import timezone
from datetime import datetime, time, timedelta
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import TruncDate

class SubjectListView(ListView):
    template_name = 'subject_list.html'
    model = Subject


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
    


class EvaluationGet(LoginRequiredMixin, DetailView):
    template_name = 'subject_detail.html'
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EvaluationForm()
        return context
    
    """uncomment this code and the understand_count and not_yet_count will work but the form will not work"""
    '''I don't understand why this is happening'''
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['understand_count'] = Evaluation.objects.filter(understand=True).count()
    #     context['not_yet_count'] = Evaluation.objects.filter(not_yet=True).count()
    #     context['both_count'] = Evaluation.objects.filter(Q(understand=True) & Q(not_yet=True)).count()

    #     # Get the current date
    #     today = timezone.now().date()

    #     # Get the datetime for the start and end of today
    #     start_of_today = timezone.make_aware(datetime.combine(today, time.min))
    #     end_of_today = timezone.make_aware(datetime.combine(today, time.max))

    #     # Count 'both_count' within today's calendar day
    #     context['both_count_today'] = Evaluation.objects.filter(
    #         Q(understand=True) & Q(not_yet=True) & Q(created_at__range=(start_of_today, end_of_today))
    #     ).count()

    #     return context


class SubjectDetailView(LoginRequiredMixin, DetailView, View):
    def get(self, request, *args, **kwargs):
        view = EvaluationGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = EvaluationPost.as_view()
        return view(request, *args, **kwargs)



class SubjectRecapView(DetailView):
    """This classed based view is a mini recap of the evaluations.
    This view is not working."""
    model = Subject
    template_name = 'subject_detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['understand_count'] = Evaluation.objects.filter(understand=True).count()
        context['not_yet_count'] = Evaluation.objects.filter(not_yet=True).count()
        context['both_count'] = Evaluation.objects.filter(Q(understand=True) & Q(not_yet=True)).count()

        # Get the current date
        today = timezone.now().date()

        # Get the datetime for the start and end of today
        start_of_today = timezone.make_aware(datetime.combine(today, time.min))
        end_of_today = timezone.make_aware(datetime.combine(today, time.max))

        # Count 'both_count' within today's calendar day
        context['both_count_today'] = Evaluation.objects.filter(
            Q(understand=True) & Q(not_yet=True) & Q(created_at__range=(start_of_today, end_of_today))
        ).count()

        return context

def subject_mini_recap(request,pk):
    """Here is the same code in funchtion based view."""
    subject = get_object_or_404(Subject, pk=pk)

    understand_count = Evaluation.objects.filter(understand=True).count()
    not_yet_count = Evaluation.objects.filter(not_yet=True).count()
    both_count = Evaluation.objects.filter(Q(understand=True) & Q(not_yet=True)).count()

    # Get the current date
    today = timezone.now().date()

    # Get the datetime for the start and end of today
    start_of_today = timezone.make_aware(datetime.combine(today, time.min))
    end_of_today = timezone.make_aware(datetime.combine(today, time.max))

    # Count 'both_count' within today's calendar day
    both_count_today = Evaluation.objects.filter(
        Q(understand=True) & Q(not_yet=True) & Q(created_at__range=(start_of_today, end_of_today))
    ).count()

    context = {
        'subject': subject,
        'understand_count': understand_count,
        'not_yet_count': not_yet_count,
        'both_count': both_count,
        'both_count_today': both_count_today,
    }

    return render(request, 'subject_detail.html', context)
    
class DashboardView(TemplateView):
    """this is the code for the dashboard tab"""
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # calculate the number of evaluations for each day of the week
        today = datetime.now()#.date()
        print('today', today)
        # get the date seven days ago
        seven_days_ago = today - timedelta(days=7)
        print('seven_days_ago', seven_days_ago)
        
        #print('date_range', date_range)

        # Query to get daily total counts of records in Evaluation where created_at is in the last 7 days, and count the number of records for each day, resulting in a list of dictionaries,
        # each dictionary containing the day (in date format) and the count of records for that day:
        weekly_eval = Evaluation.objects.filter(
                            created_at__range=(seven_days_ago, today)
                        ).annotate(
                            date=TruncDate('created_at')  # Truncate to date
                        ).values('date').annotate(
                            count=Count('id')
                        ).order_by('date')
        
        weekly_understand_eval = Evaluation.objects.filter(
                            created_at__range=(seven_days_ago, today)
                        ).annotate(
                            date=TruncDate('created_at')  
                        ).values('date').annotate(
                            count=Count('id', filter=Q(understand=True))
                        ).order_by('date')
        
        weekly_not_yet_eval = Evaluation.objects.filter(
                            created_at__range=(seven_days_ago, today)
                        ).annotate(
                            date=TruncDate('created_at')  
                        ).values('date').annotate(
                            count=Count('id', filter=Q(not_yet=True))
                        ).order_by('date')
        

        
        dates = [item['date'] for item in weekly_eval]
        dates = [item['date'] for item in weekly_understand_eval]
        dates = [item['date'] for item in weekly_not_yet_eval]
        # convert dates to string format:
        dates = [date.strftime('%Y-%m-%d') for date in dates]
        
        evals = [item['count'] for item in weekly_eval]
        understand_evals = [item['count'] for item in weekly_understand_eval]
        not_yet_evals = [item['count'] for item in weekly_not_yet_eval]
         
        print('dates', dates)
        print('evals', evals)
        print('understand_evals', understand_evals)
        print('not_yet_evals', not_yet_evals)
        # print('weekly_understand_eval', weekly_understand_eval)
        # print('weekly_not_yet_eval', weekly_not_yet_eval)


        #print('weekly_eval', weekly_eval)

        context['chartData'] = {
            'labels': dates,
            'evals': evals,
        }
        return context
    
