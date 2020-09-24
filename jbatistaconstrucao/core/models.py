from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .validators import validate_file_extension


class Portfolio(models.Model):
    name = models.CharField(_("name"), max_length=150)
    photo = models.FileField(_("photo"), validators=[validate_file_extension])
    content = RichTextUploadingField(_("content"))

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"

    def __str__(self):
        return self.name
