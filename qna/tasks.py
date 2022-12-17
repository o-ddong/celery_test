from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def task_send_email():
    subject = "message"
    to = ["odh0112@naver.com"]
    from_email = "odh0112@naver.com"
    message = "메세지 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
