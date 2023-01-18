# Generated by Django 4.1.5 on 2023-01-18 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_meta', '0003_alter_city_active_alter_city_country_and_more'),
        ('user_profile', '0003_alter_employerprofile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='active',
            field=models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='license_id_file',
            field=models.ForeignKey(blank=True, db_column='license_id_file', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_license_files', to='project_meta.media', verbose_name='License File'),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='active',
            field=models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='highest_education',
            field=models.ForeignKey(blank=True, db_column='highest_education', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_highest_educations', to='project_meta.educationlevel', verbose_name='Highest Education'),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
