# Generated by Django 4.1.5 on 2024-03-11 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrights',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='userrights',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='usersubrights',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='usersubrights',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='usersubrights',
            name='rights',
        ),
        migrations.DeleteModel(
            name='Rights',
        ),
        migrations.DeleteModel(
            name='UserRights',
        ),
        migrations.DeleteModel(
            name='UserSubRights',
        ),
    ]
