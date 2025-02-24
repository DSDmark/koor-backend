# Generated by Django 4.1.5 on 2023-11-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0043_alter_aboutus_slug_alter_content_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=455, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=455, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='faqcategory',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=455, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='resourcescontent',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=455, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=455, null=True, unique=True),
        ),
    ]
