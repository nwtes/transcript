from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TranscriptionJob(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="uploads/",null=True,blank=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="pending")
    transcription = models.TextField(blank = True,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)