# Generated by Django 4.1.5 on 2023-04-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_jobsubcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='job_sub_category',
            field=models.ManyToManyField(db_column='job_sub_category', related_name='%(app_label)s_%(class)s_job_sub_category', to='jobs.jobsubcategory', verbose_name='Job Sub Category'),
        ),
    ]
