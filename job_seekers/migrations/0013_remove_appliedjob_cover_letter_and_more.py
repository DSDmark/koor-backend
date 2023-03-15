# Generated by Django 4.1.5 on 2023-02-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0012_alter_educationrecord_education_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='cover_letter',
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='short_letter',
            field=models.TextField(blank=True, db_column='short_letter', null=True, verbose_name='Short Letter'),
        ),
    ]
