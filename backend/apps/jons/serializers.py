import os
from rest_framework import serializers
from apps.jons.models import TranscriptionJob

MAX_FILE_SIZE = 50 * 1024 * 1024

ALLOWED_EXTENSIONS = [".mp3", ".wav", ".m4a"]

ALLOWED_MIME_TYPES = [
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",
]
class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscriptionJob
        fields = ["id", "audio_file", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "status", "created_at", "updated_at"]

    def validate_audio_file(self, audio_file):


        if audio_file.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("File too large (max 50MB)")


        ext = os.path.splitext(audio_file.name)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError("Unsupported file extension")


        if audio_file.content_type not in ALLOWED_MIME_TYPES:
            raise serializers.ValidationError("Invalid file type")

        return audio_file

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscriptionJob
        fields = [
            "id",
            "status",
            "transcript",
            "created_at",
            "updated_at",
            "uploaded_file",
        ]