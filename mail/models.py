from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomerRequest(models.Model):
    name = models.CharField(_("Имя"), max_length=50)
    phone = PhoneNumberField(_('Телефон'),)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(_('Тема'), max_length=200)
    message = models.TextField(_('Сообщение'), max_length=1000)

    def __str__(self):
        return f'{self.date} - {self.name} - {self.phone}'