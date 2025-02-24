# Generated by Django 4.1.5 on 2023-05-22 11:04

from django.db import migrations, models
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0009_alter_resourcescontent_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUrl',
            fields=[
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active')),
                ('platform', models.CharField(choices=[('iso_app', 'ISO Application'), ('android_app', 'Android Application'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'Linkedin'), ('youtube', 'Youtube'), ('twitter', 'Twitter')], db_column='platform', max_length=255, verbose_name='Platform')),
                ('url', models.URLField(db_column='url', verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Social Url',
                'verbose_name_plural': 'Social Urls',
                'db_table': 'SocialUrl',
                'ordering': ['platform'],
            },
        ),
    ]
