# Generated by Django 4.1.5 on 2023-12-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_visitorlog_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_token',
            field=models.CharField(blank=True, db_column='verification_token', max_length=250, null=True, verbose_name='Verification Token'),
        ),
    ]
