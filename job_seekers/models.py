from django.db import models
from django.utils.translation import gettext as _

from core.models import (
    BaseModel, SoftDeleteModel
)
from users.models import User, TimeStampedModel
from project_meta.models import Media

class EducationRecord(BaseModel, SoftDeleteModel, TimeStampedModel, models.Model):
    """
    This Django model class represents the education record details for a job seeker. The fields are as follows:

    - `user`: The user who this education record belongs to.
    - `title`: The title of the education record.
    - `start_date`: The start date of the education record.
    - `end_date`: The end date of the education record.
    - `institute`: The institute associated with the education record.
    - `organization`: The organization associated with the education record.
    - `description`: A description of the education record.
    """
    user = models.ForeignKey(
        to=User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        db_column="user",
        related_name='%(app_label)s_%(class)s_user'
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        db_column="title",
    )
    start_date = models.DateField(
        verbose_name=_('Start Date'),
        db_column='start_date'
    )
    end_date = models.DateField(
        verbose_name=_('End Date'),
        blank=True,
        null=True,
        db_column='end_date'
    )
    institute = models.CharField(
        verbose_name=_('Institute'),
        max_length=255,
        db_column="institute",
    )
    organization = models.CharField(
        verbose_name=_('Organization'),
        max_length=255,
        db_column="organization",
    )
    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
        db_column="description",
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Education Record"
        verbose_name_plural = "Education Records"
        db_table = "EducationRecord"

class EmploymentRecord(BaseModel, SoftDeleteModel, TimeStampedModel, models.Model):
    """
    This Django model class represents the employment record details for a job seeker.

    Columns
    - `user`: The user who this employment record belongs to.
    - `title`: The title of the employment record.
    - `start_date`: The start date of the employment record.
    - `end_date`: The end date of the employment record.
    - `organization`: The organization associated with the employment record.
    - `description`: A description of the employment record.
    """
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        db_column="user",
        related_name='%(app_label)s_%(class)s_user'
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        db_column="title",
    )
    start_date = models.DateField(
        verbose_name=_('Start Date'),
        db_column='start_date'
    )
    end_date = models.DateField(
        verbose_name=_('End Date'),
        blank=True,
        null=True,
        db_column='end_date'
    )
    organization = models.CharField(
        verbose_name=_('Organization'),
        max_length=255,
        db_column="organization",
    )
    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
        db_column="description",
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Employment Record"
        verbose_name_plural = "Employment Records"
        db_table = "EmploymentRecord"

class Resume(BaseModel, SoftDeleteModel, TimeStampedModel, models.Model):
    """
    This Django model class represents the resume for a job seeker. The fields are as follows:

    - `user`: The user who this resume belongs to.
    - `title`: The title of the resume.
    - `file_path`: The file containing the resume.
    """
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        db_column="user",
        related_name='%(app_label)s_%(class)s_user'
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        db_column="title",
    )
    file_path = models.OneToOneField(
        Media,
        verbose_name=_('File Path'),
        on_delete=models.CASCADE,
        db_column="file_path",
        related_name='%(app_label)s_%(class)s_file_path'
    )

    def __str__(self):
        return str(self.title) + "(" + str(self.user) + ")"

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"
        db_table = "Resume"
