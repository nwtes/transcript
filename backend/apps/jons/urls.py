from django.urls import path
from .views import UploadVideoView, JobListView, JobDetailView



urlpatterns = [
    path('upload', UploadVideoView.as_view(),name="upload"),
    path("jobs/", JobListView.as_view()),
    path("jobs/<int:pk>/", JobDetailView.as_view()),

]
