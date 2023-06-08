# Generated by Django 4.1.5 on 2023-05-30 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0016_rename_sector_opportunitytype_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0004_vendorsector'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorTag',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('tag', models.ForeignKey(db_column='tag', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tag', to='project_meta.tag', verbose_name='Tag')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Vendor Tag',
                'verbose_name_plural': 'Vendor Tags',
                'db_table': 'VendorTag',
                'ordering': ['-created'],
            },
        ),
    ]
