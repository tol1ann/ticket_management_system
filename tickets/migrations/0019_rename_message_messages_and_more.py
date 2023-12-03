# Generated by Django 4.2.7 on 2023-12-03 18:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0018_message_ticket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Messages',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='message',
            new_name='messages',
        ),
    ]