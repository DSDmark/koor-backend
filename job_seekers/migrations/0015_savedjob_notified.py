# Generated by Django 4.1.5 on 2023-03-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0014_alter_appliedjob_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedjob',
            name='notified',
            field=models.BooleanField(blank=True, db_column='notified', default=False, null=True, verbose_name='Notified'),
        ),
    ]
