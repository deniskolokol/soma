from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .utils import deep_update


PRIVACY = (
    ('private', 'Private'),
    ('public', 'Public'),
    )



def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


def user_directory_path(instance, filename):
    """File will be uploaded to MEDIA_ROOT/user_<id>/<filename>"""
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class DictDocumentMixin(object):
    @property
    def _dict(self):
        try:
            _dict = dict((f, getattr(self, f)) for f in self._fields)
        except (KeyError, AttributeError):
            return self.__dict__

        return deep_update(_dict, self.__dict__)


class NamedModel(models.Model, DictDocumentMixin):
    """
    Abstract class for all vocabulary-like models.
    """
    name = models.CharField(max_length=255, db_index=True, help_text=_(u'Name'))
    note = models.TextField(null=True, blank=True, help_text=_(u'Note'))
    created = models.DateTimeField(auto_now_add=True, help_text=_(u'Created'))
    updated = models.DateTimeField(auto_now=True, help_text=_(u'Last updated'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class NamedUserModel(NamedModel):
    """
    Abstract class for vocabulary-like models,
    whose records belong to specific users.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        )

    class Meta:
        abstract = True

    def __str__(self):
        return "%s (%s)" % (self.name, self.user.username)


class TaggedUserModel(NamedUserModel):
    """
    Multi-purpose user-based tag model, where the field `name` serves as a tag.
    Examples:
        Segments of practice for a particular user such as 'Doable', 'Attempt',
        <name of tradition>, etc.
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class TaggedModel(NamedModel):
    """
    Multi-purpose tag model, where the field `name` serves as a tag.
    Can be attached to any other model without mentioning a user.
    Internal use only!
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class TaggedUserItem(TaggedUserModel):
    def __str__(self):
        parent_str = super().__str__()
        return "#%s %s:%s:%d" % (
            parent_str,
            self.content_type.app_label,
            self.content_type.model,
            self.object_id
            )


class Score(NamedUserModel):
    """
    Multi-purpose user-based score model, where the field `name` is a score name
    (for example, "Difficulty", "Effectiveness", etc.).
    """
    privacy = models.CharField(
        choices=PRIVACY,
        max_length=25,
        default='private'
        )
    # TODO - pre_save signal to check that maxval > minval
    minval = models.PositiveIntegerField()
    maxval = models.PositiveIntegerField()


class ScoredItem(TaggedModel):
    """
    Multi-purpose user-based score model.
    """
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    val = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s %s:%d to %s:%s:%d" % (
            self.score.user.username,
            self.score.name,
            self.val,
            self.content_type.app_label,
            self.content_type.model,
            self.object_id
            )


class ImageUser(TaggedUserItem):
    """
    Illustration that can be attached by user to an arbitrary model.
    Example: image of a particular form of Asana, which serves as a
             reference to a particular user, but not to others.
    """
    img = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        parent_str = super().__str__()
        return "%s - %s" % (parent_str, self.url)
