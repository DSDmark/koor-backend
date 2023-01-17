from django.db import models
from django.utils.translation import gettext as _

from autoslug import AutoSlugField

from core.models import (
    BaseModel, upload_directory_path, SoftDeleteModel
)


class Media(BaseModel, models.Model):
    MEDIA_TYPE_CHOICE = (
        ('image', "Image"),
        ('video', "Video"),
        ('document', "Document"),
    )

    file_path = models.FileField(
        verbose_name=_('File Path'),
        unique=True,
        upload_to=upload_directory_path,
        db_column="file_path",
    )
    media_type = models.CharField(
        verbose_name=_('Media Type'),
        max_length=250,
        db_column="media_type",
        choices=MEDIA_TYPE_CHOICE,
        default='image'
    )

    def __str__(self):
        return self.file_path

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"
        db_table = "Media"


class Tag(BaseModel, SoftDeleteModel, models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        db_column="title",
    )
    slug = AutoSlugField(
        populate_from='title',
        always_update=True,
        unique=True,
        null=True,
        blank=True,
        db_column="slug",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = "Tag"


class Language(BaseModel, SoftDeleteModel, models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        db_column="title",
    )
    slug = AutoSlugField(
        populate_from='title',
        always_update=True,
        unique=True,
        null=True,
        blank=True,
        db_column="slug",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        db_table = "Language"
