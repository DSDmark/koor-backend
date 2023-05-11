# Generated by Django 4.1.5 on 2023-05-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0014_delete_jobseekercategory'),
        ('tenders', '0004_remove_tenderfilter_budget_tenderfilter_budget_max_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenderdetails',
            name='sector',
        ),
        migrations.AddField(
            model_name='tenderdetails',
            name='sector',
            field=models.ManyToManyField(db_column='sector', related_name='%(app_label)s_%(class)s_sectors', to='project_meta.sector', verbose_name='Sector'),
        ),
    ]
