from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.shortcuts import render, redirect

# em = EmailMessage(subject='test20', body='Test', to=['remont199@gmail.com'])
# em.send()
from django.urls import reverse

from .models import CustomerRequest

from django.views.generic import TemplateView, CreateView
from .forms import MailForm, CustomerRequestForm


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
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_TO, ]
            message = request.POST.get("message")
            feedback = f'{name} - {phone} - {subject}'
            EmailMessage(feedback, message, email_from, recipient_list, connection=connection).send()

        messageSent = True
    return render(request, 'mail/home.html', {
        'recipient': recipient_list,
        'messageSent': messageSent,
        'send_method': 'def send_email(request):',
    })


class HomeView(TemplateView):
    # template_name = 'mail/class_email.html'
    template_name = 'mail/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mail_form'] = MailForm
        context['send_method'] = 'class HomeView(TemplateView):'
        return context


class CustomerRequestView(TemplateView):
    template_name = 'mail/class_email.html'

    # template_name = 'mail/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomerRequestForm
        context['send_method'] = 'class CustomerRequestView(TemplateView):'
        return context


class EmailSend(CreateView):
    form_class = MailForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return send_email(request)


class CustomerRequestSend(CreateView):
    form_class = CustomerRequestForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            return send_email(request)
        else:
            context = {'form': form}
            # return redirect(reverse('cust_req'))
            return render(request, 'mail/class_email.html', context)
