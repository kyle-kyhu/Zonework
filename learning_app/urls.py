from django.urls import path, include

from .views import SummaryListView, HomeListView

urlpatterns = [
    path("summary/", SummaryListView.as_view(), name="summary"),
    path("", HomeListView.as_view(), name="home")
]
