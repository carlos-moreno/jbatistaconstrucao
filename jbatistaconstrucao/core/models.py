from django.db import models
from froala_editor.fields import FroalaField
from .validators import validate_file_extension
from django.utils.translation import ugettext_lazy as _


class Portfolio(models.Model):
    name = models.CharField(_("name"), max_length=150)
    photo = models.FileField(_("photo"), validators=[validate_file_extension])
    content = FroalaField(_("content"), theme="dark")

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"

    def __str__(self):
        return self.name
