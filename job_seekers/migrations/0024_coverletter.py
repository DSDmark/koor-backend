# Generated by Django 4.1.5 on 2024-01-05 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0032_alter_jobdetails_city'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_meta', '0019_alter_choice_slug_alter_city_slug_alter_country_slug_and_more'),
        ('job_seekers', '0023_jobpreferences_pay_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, db_column='job_title', max_length=250, null=True, verbose_name='Job Title')),
                ('name_or_address', models.CharField(blank=True, db_column='name_or_address', max_length=250, null=True, verbose_name='Name or Address')),
                ('cover_letter', models.TextField(blank=True, db_column='cover_letter', null=True, verbose_name='Cover Letter')),
                ('job', models.ForeignKey(db_column='job', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_job', to='jobs.jobdetails', verbose_name='Job')),
                ('signature', models.OneToOneField(blank=True, db_column='signature', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_signature', to='project_meta.media', verbose_name='Signature')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Cover Letter',
                'verbose_name_plural': 'Cover Letters',
                'db_table': 'CoverLetter',
            },
        ),
    ]
