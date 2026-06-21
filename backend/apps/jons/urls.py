from django.urls import path
from .views import UploadAndCreateJobView, JobListView, JobDetailView



urlpatterns = [
    path('upload', UploadAndCreateJobView.as_view(),name="upload"),
    path("jobs/", JobListView.as_view()),
    path("jobs/<int:pk>/", JobDetailView.as_view()),

]
