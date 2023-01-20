# Generated by Django 4.1.5 on 2023-01-18 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0003_alter_city_active_alter_city_country_and_more'),
        ('users', '0002_alter_user_image_alter_usersession_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_column='email', max_length=254, null=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ForeignKey(blank=True, db_column='image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_image', to='project_meta.media', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='active',
            field=models.BooleanField(blank=True, db_column='active', default=True, null=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='agent',
            field=models.JSONField(db_column='agent', null=True, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='expire_at',
            field=models.DateTimeField(blank=True, db_column='expire_at', null=True, verbose_name='Expire At'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, db_column='ip_address', null=True, verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
