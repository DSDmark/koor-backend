# Generated by Django 4.1.5 on 2023-04-06 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_meta', '0007_remove_jobseekercategory_active_and_more'),
        ('tenders', '0002_tenderdetails_deadline_tenderdetails_start_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderFilter',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active')),
                ('title', models.TextField(db_column='title', verbose_name='Title')),
                ('opportunity_type', models.CharField(blank=True, choices=[('government', 'Government'), ('ngo', 'NGO'), ('business', 'Business')], db_column='opportunity_type', max_length=105, null=True, verbose_name='Opportunity Type')),
                ('sector', models.CharField(blank=True, choices=[('ngo', 'NGO'), ('private', 'Private'), ('public', 'Public')], db_column='sector', max_length=105, null=True, verbose_name='Sector')),
                ('deadline', models.DateField(blank=True, db_column='deadline', null=True, verbose_name='Deadline')),
                ('budget', models.DecimalField(blank=True, db_column='budget', decimal_places=2, max_digits=19, null=True, verbose_name='Budget')),
                ('is_notification', models.BooleanField(blank=True, db_column='is_notification', null=True, verbose_name='Is Notification')),
                ('city', models.ForeignKey(blank=True, db_column='city', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_city', to='project_meta.city', verbose_name='City')),
                ('country', models.ForeignKey(blank=True, db_column='country', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_country', to='project_meta.country', verbose_name='Country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('tag', models.ManyToManyField(blank=True, db_column='tag', null=True, related_name='%(app_label)s_%(class)s_tags', to='project_meta.tag', verbose_name='Tag')),
                ('tender_category', models.ManyToManyField(blank=True, db_column='tender_category', null=True, related_name='%(app_label)s_%(class)s_tender_category', to='tenders.tendercategory', verbose_name='Tender Category')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Tender Filter',
                'verbose_name_plural': 'Tender Filters',
                'db_table': 'TenderFilter',
                'ordering': ['-created'],
            },
        ),
    ]
