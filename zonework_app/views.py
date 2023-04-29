from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import View, ListView
from .models import LearningItem, Student
from .forms import ItemForm


# Create your views here.

#@login_required
class DashboardView(View):
    template_name = 'zonework_app/dashboard.html'

    def get(self, request):
        student, created = Student.objects.get_or_create(user=request.user)
        items = LearningItem.objects.filter(student=student)
        return render(request, self.template_name, {'items': items})


#@login_required
class LearningView(View):
    template_name = 'zonework_app/learning_tab.html'

    def get(self, request):
        form = ItemForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.student = request.user.student
            new_item.save()
            return redirect("zonework_app:dashboard")
        else:
            return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'zonework_app/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('zonework_app:dashboard'))
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, self.template_name)


class RegisterView(View):
    template_name = 'zonework_app/register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student(user=user)
            student.save()
            return redirect('zonework_app:login')
        else:
            return render(request, self.template_name, {'form': form})


class DashboardListView(ListView):
    template_name = 'zonework_app/dashboard.html'
    context_object_name = 'items'

    def get_queryset(self):
        student, created = Student.objects.get_or_create(user=self.request.user)
        queryset = LearningItem.objects.filter(student=student)
        return queryset


class IndexView(View):
    template_name = 'zonework_app/index.html'

    def get(self, request):
        return render(request, self.template_name)


