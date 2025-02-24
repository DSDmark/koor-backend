# Generated by Django 4.1.5 on 2023-04-26 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0020_appliedjob_interview_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedjobattachmentsitem',
            name='applied_job',
            field=models.ForeignKey(db_column='applied_job', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_applied_job', to='job_seekers.appliedjob', verbose_name='Applied Job'),
        ),
    ]
