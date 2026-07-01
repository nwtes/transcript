import time

from celery import shared_task

from apps.jons.models import ProcessingJob


@shared_task
def process_video(job_id):
    job = ProcessingJob.objects.get(id=job_id)
    try:
        print("0%")
        job.status = "processing"
        job.save()
        print("25%")
        time.sleep(10)
        print("75%")
        job.status = "completed"
        job.save()
        print("100%")
    except Exception as e:
        print("error" + str(e))
        job.status = "failed"
        job.error_message = str(e)
        job.save()