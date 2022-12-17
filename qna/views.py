from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework.response import Response

from .tasks import task_send_email


# Create your views here.


def send_email(request):

    try:
        print("send_email에 진입했습니다.")
        task_send_email.delay()
        print("email을 성공적으로 보냈습니다.")
        return Response("성공했습니다.")
    except Exception as e:
        return Response("성공적으로 보내지 못했습니다.")