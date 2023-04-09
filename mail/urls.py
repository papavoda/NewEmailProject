
from django.contrib import admin
from django.urls import path, include

from .views import HomeView, EmailSend, send_email, CustomerRequestView, CustomerRequestSend

urlpatterns = [
    # "Class based email send"
    path("", HomeView.as_view(), name='home'),
    path('email/', EmailSend.as_view(), name="email_send"),

    # Class based send and save in database as CustomerRequest
    path('cust-req/', CustomerRequestView.as_view(), name='cust_req'),
    path('send/', CustomerRequestSend.as_view(), name='send'),

    # Function for send email
    path("send-email/", send_email, name='send_email'),
]

