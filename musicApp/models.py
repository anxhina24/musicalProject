from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
"""
Works model .
"""
import uuid

from django.db import models


class Works(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    iswc = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='iswc',
        blank=False, null=False
    )

    title = models.CharField(
        verbose_name='title',
        blank=False, null=False,
        max_length=255

    )
    contributors = ArrayField(models.CharField(blank=True, null=True, max_length=255), blank=False, null=False)