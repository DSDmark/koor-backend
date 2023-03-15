# Generated by Django 4.1.5 on 2023-02-02 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("job_seekers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmploymentRecord",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                (
                    "id",
                    model_utils.fields.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        blank=True,
                        db_column="active",
                        default=True,
                        null=True,
                        verbose_name="Active",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_column="title", max_length=255, verbose_name="Title"
                    ),
                ),
                (
                    "start_date",
                    models.DateField(db_column="start_date", verbose_name="Start Date"),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True,
                        db_column="end_date",
                        null=True,
                        verbose_name="End Date",
                    ),
                ),
                (
                    "organization",
                    models.CharField(
                        db_column="organization",
                        max_length=255,
                        verbose_name="Organization",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        db_column="description",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created By",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified By",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_column="user",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Employment Record",
                "verbose_name_plural": "Employment Records",
                "db_table": "EmploymentRecord",
            },
        ),
    ]
