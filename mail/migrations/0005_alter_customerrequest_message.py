# Generated by Django 4.1.7 on 2023-04-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_alter_customerrequest_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='message',
            field=models.TextField(max_length=1000, verbose_name='Сообщение'),
        ),
    ]
