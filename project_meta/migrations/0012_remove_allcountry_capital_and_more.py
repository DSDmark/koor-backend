# Generated by Django 4.1.5 on 2023-04-28 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_meta', '0011_allcity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcountry',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='currency_name',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='currency_symbol',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='emoji',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='emojiU',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='native',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='numeric_code',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='region',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='subregion',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='timezones',
        ),
        migrations.RemoveField(
            model_name='allcountry',
            name='tld',
        ),
    ]
