
from django.contrib import admin
from django.urls import path, include

from .views import HomeView, EmailSend, send_email

urlpatterns = [
    # "Class based email send"
    path("", HomeView.as_view(), name='home'),
    path('email/', EmailSend.as_view(), name="email_send"),
    # Function for sen email
    path("send-email/", send_email),
]

