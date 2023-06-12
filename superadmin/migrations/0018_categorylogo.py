# Generated by Django 4.1.5 on 2023-06-08 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_meta', '0016_rename_sector_opportunitytype_and_more'),
        ('superadmin', '0017_alter_resourcescontent_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLogo',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('logo', models.OneToOneField(db_column='logo', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_logo', to='project_meta.media', verbose_name='Logo')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'verbose_name': 'CategoryLogo',
                'verbose_name_plural': 'Category Logos',
                'db_table': 'CategoryLogo',
                'ordering': ['-created'],
            },
        ),
    ]
