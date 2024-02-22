# Generated by Django 4.1.5 on 2024-02-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_verification_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(db_column='is_company', default=False, verbose_name='Is Company'),
        ),
    ]
