# Generated by Django 4.1.5 on 2023-05-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0016_rename_sector_opportunitytype_and_more'),
        ('tenders', '0012_remove_tenderdetails_sector_tenderdetails_sectors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenderdetails',
            name='sectors',
        ),
        migrations.AddField(
            model_name='tenderdetails',
            name='sector',
            field=models.ManyToManyField(db_column='sector', related_name='%(app_label)s_%(class)s_sectors', to='project_meta.choice', verbose_name='Sector'),
        ),
    ]
