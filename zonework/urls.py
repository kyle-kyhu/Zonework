from django.urls import path

from .views import (
    SubjectListView,
    SujbectDetailView,
    DashboardView,  
)


urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("<int:pk>/", SujbectDetailView.as_view(), name="subject_detail"),
    path("", SubjectListView.as_view(), name="subject_list"),
]