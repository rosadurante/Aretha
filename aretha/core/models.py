from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.db import models
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField


class BasePublication(models.Model):
    """
    Abstract model that will be used as the basic kind of publication
    """
    title = models.CharField(
        verbose_name=_('Title'), max_length=100)
    slug = models.CharField(
        verbose_name=_('Slug'), max_length=100, unique=True,
        validators=[validate_slug])
    author = models.ForeignKey(
        User, verbose_name=_('Author'), on_delete=models.SET_NULL)
    created_at = models.DateTimeField(
        verbose_name=_('Created at'), auto_now_add=True)
    last_modified = models.DateTimeField(
        verbose_name=_('Last modification'), auto_now=True)
    body = models.TextField(verbose_name=_('Body'))
    tags = TagField(verbose_name=_('Tags'),
                    help_text=_('Tags will be splitted by commas'))

    class Meta:
        abstract = True
        verbose_name = _('Base publication')
        verbose_name_plural = _('Base publications')


class Publication(BasePublication):
    related_link = models.UrlField(
        verbose_name=_('Related link'), verify_exists=False)
    is_published = models.BooleanField(
        verbose_name=_('Published'), default=False)

    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publication')

    def __unicode__(self):
        return self.slug
