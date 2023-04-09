from django import forms
from .models import CustomerRequest
from phonenumber_field.formfields import PhoneNumberField


class MailForm(forms.Form):
    # required_css_class = 'form-control'
    name = forms.CharField(widget=forms.TextInput, label='Имя', max_length=50, required=True)
    phone = forms.CharField(label='Телефон', max_length=20, required=True)
    subject = forms.CharField(label='Тема', max_length='50', required=True)
    message = forms.CharField(widget=forms.Textarea, label='Сообщение', max_length='500', required=True)


class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        exclude = ('date',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите Ваше Имя *', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефона (например 9031234567) *', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема сообщения *', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': '', 'class': 'form-control'}),
        }
