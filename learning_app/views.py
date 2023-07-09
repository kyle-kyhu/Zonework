from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    FormView,
    DetailView,
)
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
    


class LearningPageView(CreateView): # this is similar to the detail view
    model = LearningItem
    #form_class = ItemForm
    template_name = "learning.html"
    fields = ["text"]
    #success_url = reverse_lazy('home')

# def post(self, request, *args, **kwargs):
#     self.object = self.get_object()
#     return super().post(request, *args, **kwargs)

# def form_valid(self, form):
#     pass


"""THis is the snippet form the orginal code"""
# class LearningPageView(View):
#     def get(self, request):
#         learning_items = LearningItem.objects.order_by('-entry_date')
#         context = {
#             'form': ItemForm(),
#             'learning_items': learning_items,
#         }
#         return render(request, 'learning.html', context)

#     def post(self, request):
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             new_item = form.save(commit=False)
#             new_item.student = request.user.student
#             new_item.save()
#             return redirect("/learning")

#         learning_items = LearningItem.objects.order_by('-entry_date')
#         context = {
#             'form': form,
#             'learning_items': learning_items,
#         }
#         return render(request, 'learning.html', context)


class DashboardPageView(ListView):
    model = LearningItem
    template_name = "dashboard.html"

class AboutPageView(TemplateView):
    template_name = "about.html"