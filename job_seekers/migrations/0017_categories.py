# Generated by Django 4.1.5 on 2023-03-31 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0007_remove_jobseekercategory_active_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_seekers', '0016_jobpreferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active')),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_categories', to='project_meta.jobseekercategory', verbose_name='Category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Categories',
                'ordering': ['-created'],
            },
        ),
    ]
