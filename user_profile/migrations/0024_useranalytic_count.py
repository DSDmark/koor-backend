# Generated by Django 4.1.5 on 2023-07-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0023_useranalytic'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranalytic',
            name='count',
            field=models.BigIntegerField(blank=True, db_column='count', default=0, null=True, verbose_name='Count'),
        ),
    ]
