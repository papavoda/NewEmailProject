from django import forms


class MailForm(forms.Form):
    # required_css_class = 'form-control'
    name = forms.CharField(widget=forms.TextInput, label='Имя', max_length=50, required=True)
    phone = forms.CharField(label='Телефон', max_length=20, required=True)
    subject = forms.CharField(label='Тема', max_length='50', required=True )
    message = forms.CharField(widget=forms.Textarea, label='Сообщение', max_length='500', required=True )

