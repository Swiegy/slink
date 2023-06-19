import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class LinkModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("Shorted URL Hash"))

    url = models.URLField(max_length=2048, blank=False, null=False, verbose_name=_("Target URL"))

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = ("Links")
        ordering = ('-url', '-id')
