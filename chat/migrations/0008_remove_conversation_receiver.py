# Generated by Django 4.1.5 on 2023-07-04 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_conversation_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='receiver',
        ),
    ]
