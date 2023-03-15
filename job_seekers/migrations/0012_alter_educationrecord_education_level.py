# Generated by Django 4.1.5 on 2023-02-17 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0004_media_title'),
        ('job_seekers', '0011_remove_educationrecord_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationrecord',
            name='education_level',
            field=models.ForeignKey(db_column='education_level', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_education', to='project_meta.educationlevel', verbose_name='Education Level'),
        ),
    ]
