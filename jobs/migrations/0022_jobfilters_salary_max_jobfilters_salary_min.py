# Generated by Django 4.1.5 on 2023-04-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_jobfilters_job_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfilters',
            name='salary_max',
            field=models.CharField(blank=True, db_column='salary_max', max_length=250, null=True, verbose_name='Salary Max'),
        ),
        migrations.AddField(
            model_name='jobfilters',
            name='salary_min',
            field=models.CharField(blank=True, db_column='salary_min', max_length=250, null=True, verbose_name='Salary Min'),
        ),
    ]
