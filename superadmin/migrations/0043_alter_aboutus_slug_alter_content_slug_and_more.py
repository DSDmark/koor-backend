# Generated by Django 4.1.5 on 2023-11-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0042_alter_googleaddsensecode_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='faqcategory',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='resourcescontent',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='slug',
            field=models.SlugField(blank=True, db_column='slug', max_length=255, null=True, unique=True),
        ),
    ]
