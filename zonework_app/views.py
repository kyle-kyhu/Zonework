from django.shortcuts import render, redirect
from .models import Item, Student
from .forms import ItemForm
from django.contrib import messages

from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# this one is new as of 4/16/23
from django.contrib.auth.views import LoginView


# Create your views here.

@login_required
#a list of all items belonging to a student
def dashboard(request):
    # Get or create the student instance for the logged-in user
    student, created = Student.objects.get_or_create(user=request.user)

    # Query for items for the logged in student
    items = Item.objects.filter(student=student)
    return render(request, 'zonework_app/dashboard.html', {'items': items})


@login_required
def learning_tab(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.student = request.user.student
            new_item.save()
            return redirect("dashboard")
    else:
        form = ItemForm()
    return render(request, 'zonework_app/learning_tab.html', {'form':form})

from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            return redirect(reverse('zonework_app:dashboard'))  # Use reverse with the namespaced view name
        else:
            # Add an error message to display on the login page if the authentication fails
            messages.error(request, 'Invalid username or password')
    return render(request, 'zonework_app/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student(user=user)
            student.save()
            # You can create a Student instance related to the User here.
            return redirect('zonework_app/login')
    else:
        form = UserCreationForm()
    return render(request, 'zonework_app/register.html', {'form': form})

def index(request):
    return render(request, 'zonework_app/index.html')

# here are tests
def test(request):
    return render(request, 'zonework_app/test.html')

def nav_bar(request):
    return render(request, 'zonework_app/nav_bar.html')