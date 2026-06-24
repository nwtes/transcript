import time

from celery import shared_task

from apps.jons.models import ProcessingJob


@shared_task
def process_video(job_id):
    job = ProcessingJob.objects.get(job_id=job_id)
    try:
        job.status = "processing"
        job.save()
        time.sleep(10)
        job.status = "completed"
        job.save()
    except Exception as e:
        job.status = "failed"
        job.error_message = str(e)
        job.save()