# Generated by Django 4.1.5 on 2023-05-22 16:19

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
        ('tenders', '0013_remove_tenderdetails_sectors_tenderdetails_sector'),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedTender',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active')),
                ('shortlisted_at', models.DateTimeField(blank=True, db_column='shortlisted_at', null=True, verbose_name='Short Listed At')),
                ('rejected_at', models.DateTimeField(blank=True, db_column='rejected_at', null=True, verbose_name='Rejected At')),
                ('short_letter', models.TextField(blank=True, db_column='short_letter', null=True, verbose_name='Short Letter')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('tender', models.ForeignKey(db_column='tender', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tender', to='tenders.tenderdetails', verbose_name='Tender')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Applied Tender',
                'verbose_name_plural': 'Applied Tenders',
                'db_table': 'AppliedTender',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AppliedTenderAttachmentsItem',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active')),
                ('applied_tender', models.ForeignKey(db_column='applied_tender', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_applied_tender', to='vendors.appliedtender', verbose_name='Applied Tender')),
                ('attachment', models.OneToOneField(blank=True, db_column='attachment', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_attachment', to='project_meta.media', verbose_name='Attachment')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
            options={
                'verbose_name': 'Applied Tender Attachment Item',
                'verbose_name_plural': 'Applied Tender Attachment Items',
                'db_table': 'AppliedTenderAttachmentsItem',
                'ordering': ['-created'],
            },
        ),
    ]
