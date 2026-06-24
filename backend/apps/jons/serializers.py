import os
from .models import Video
from rest_framework import serializers
from .models import ProcessingJob

MAX_FILE_SIZE = 500 * 1024 * 1024

ALLOWED_EXTENSIONS = [".mp4", ".mov", ".mkv", ".avi"]


class VideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "video_file", "title"]

    def validate_video_file(self, file):
        if file.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("File too large")

        ext = os.path.splitext(file.name)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError("Unsupported video type")

        return file



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingJob
        fields = "__all__"