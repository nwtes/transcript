from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TranscriptionJob
from .serializers import UploadedFileSerializer, JobSerializer


# Create your views here.



class UploadAndCreateJobView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_serializer = UploadedFileSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)

        uploaded_file = file_serializer.save(user=request.user)

        job = TranscriptionJob.objects.create(
            user=request.user,
            uploaded_file=uploaded_file,
            status="pending"
        )

        return Response({
            "job_id": job.id,
            "status": job.status
        }, status=201)

class JobListView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TranscriptionJob.objects.filter(user=self.request.user)

class JobDetailView(RetrieveAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TranscriptionJob.objects.filter(user=self.request.user)