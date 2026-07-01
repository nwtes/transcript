from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import process_video
from .models import ProcessingJob
from .serializers import JobSerializer, VideoUploadSerializer


# Create your views here.





class UploadVideoView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        serializer = VideoUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = serializer.save(user=request.user)

        job = ProcessingJob.objects.create(
            user=request.user,
            video=video,
            status="pending"
        )

        print("1")
        process_video.delay(job.id)
        print("2")
        return Response({
            "video_id": video.id,
            "job_id": job.id,
            "status": job.status
        }, status=status.HTTP_201_CREATED)


class JobListView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProcessingJob.objects.filter(user=self.request.user)

class JobDetailView(RetrieveAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProcessingJob.objects.filter(user=self.request.user)