from django.urls import path

from .views import (
    SubjectListView,
    SubjectDetailView,
    SubjectUpdateView,
    SubjectDeleteView,
    SubjectCreateView
)

urlpatterns = [
    path("<int:pk>/", SubjectDetailView.as_view(), name="subject_detail"),
    path("<int:pk>/edit/", SubjectUpdateView.as_view(), name="subject_edit"),
    path("<int:pk>/delete/", SubjectDeleteView.as_view(), name="subject_delete"),
    path("new/", SubjectCreateView.as_view(), name="subject_new"),
    path("", SubjectListView.as_view(), name="subject_list"),
]
