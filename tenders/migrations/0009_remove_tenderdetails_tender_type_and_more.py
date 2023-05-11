# Generated by Django 4.1.5 on 2023-05-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0016_rename_sector_opportunitytype_and_more'),
        ('tenders', '0008_remove_tenderdetails_sector_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenderdetails',
            name='tender_type',
        ),
        migrations.RemoveField(
            model_name='tenderfilter',
            name='opportunity_type',
        ),
        migrations.AddField(
            model_name='tenderdetails',
            name='tender_type',
            field=models.ManyToManyField(db_column='tender_type', related_name='%(app_label)s_%(class)s_tender_type', to='project_meta.opportunitytype', verbose_name='Tender Type'),
        ),
        migrations.AddField(
            model_name='tenderfilter',
            name='opportunity_type',
            field=models.ManyToManyField(db_column='opportunity_type', related_name='%(app_label)s_%(class)s_opportunity_types', to='project_meta.opportunitytype', verbose_name='Opportunity Type'),
        ),
    ]
