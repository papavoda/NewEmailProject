from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.shortcuts import render


def send_email(request):
    messageSent = ''
    recipient_list = ''
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"), ]
            message = request.POST.get("message")
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

        messageSent = True
    return render(request, 'mail.home.html', {
        'recipient': recipient_list,
        'messageSent': messageSent,
    })
