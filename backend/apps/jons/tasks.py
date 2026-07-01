import subprocess
import time

from celery import shared_task
import os
from apps.jons.models import ProcessingJob
from config import settings


@shared_task
def process_video(job_id):
    job = ProcessingJob.objects.get(id=job_id)
    try:
        print("0%")
        job.status = "processing"
        job.save()
        print("25%")
        video_path = job.video.video_file.path
        audio_path = os.path.join(settings.MEDIA_ROOT, "audio", f"{job.id}.wav")
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)

        result = subprocess.run([
                "ffmpeg",
                "-y",
                "-i", video_path,
                "-ac", "1",
                "-ar", "16000",
                audio_path
            ], check=True)
        print(result.stdout)
        print(result.stderr)
        print(result.returncode)
        print("75%")
        job.status = "completed"
        job.save()
        print("100%")
    except Exception as e:
        print("error" + str(e))
        job.status = "failed"
        job.error_message = str(e)
        job.save()