from django.contrib import admin
from django.urls import path
from . import views
from .views import LearningView, LoginView, RegisterView, IndexView, DashboardListView


app_name = 'zonework_app'

#function based set up

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('learning_tab/', views.learning_tab, name="learning_tab"),
#     path('login/', views.login_view, name='login'),
#     path('dashboard/', views.dashboard, name="dashboard"),
#     path('register/', views.register, name="register"),
#     path('test/', views.test, name="test"),
#     path('', views.index, name="index"),
# ]

# class based views
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
    path('learning/', LearningView.as_view(), name='learning_tab'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]