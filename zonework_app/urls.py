from django.contrib import admin
from django.urls import path
from . import views


app_name = 'zonework_app'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('learning_tab/', views.learning_tab, name="learning_tab"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('test/', views.test, name="test"),
    path('index/', views.index, name="index"),
]