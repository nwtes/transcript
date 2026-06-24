from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to="videos/")
    title = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.id}"

class ProcessingJob(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("transcribing", "Transcribing"),
        ("summarizing", "Summarizing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")

    transcript = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
