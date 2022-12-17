
from django.core.mail import EmailMessage

from config.celery import app


@app.task
def task_send_email():
    print("email 들어왔나요?")
    subject = "message"
    to = ["odh0112@naver.com"]
    from_email = "odh0112@naver.com"
    message = "메세지 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
