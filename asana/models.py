from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe

from core.models import NamedModel


class Asana(NamedModel):
    """
    Main asanas reference. Each asana can contain 1 to N forms (see AsanaForm).
    """
    pass


class AsanaForm(models.Model):
    asana = models.ForeignKey(
        Asana,
        related_name='forms',
        on_delete=models.CASCADE
        )
    variant = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )
    pict = models.ImageField(
        max_length=255,
        upload_to='asana/pict/',
        height_field='pict_height',
        width_field='pict_width',
        help_text=_(u'Pictogram 100x100px')
        )
    pict_height = models.IntegerField(
        default=100,
        validators=[MinValueValidator(1)]
        )
    pict_width = models.IntegerField(
        default=100,
        validators=[MinValueValidator(1)]
        )

    @property
    def name(self):
        if self.variant:
            return "%s %d" % (self.asana.name, self.variant)
        return self.asana.name

    @property
    def pict_100x100(self):
        img_url = settings.MEDIA_URL \
            + self.__class__.pict.field.upload_to \
            + self.pict.name.rsplit("/", 1)[-1]
        return mark_safe('<img src="%s" width="100" height="100" />' % img_url)

    def __unicode__(self):
        return self.name
