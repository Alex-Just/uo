from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from apps.common.behaviors import Publishable
from apps.common.fields import CustomForeignKey


class Topic(Publishable):
    pos = models.PositiveSmallIntegerField(_('Position'), unique=True)

    title = models.CharField(_('Title of Topic'), max_length=256, unique=True)

    def __str__(self):
        return f'id={self.id}, pos={self.pos}, title="{self.title[:25]}"'


class Lesson(Publishable):
    topic = CustomForeignKey(Topic, verbose_name=_('Topic'), related_name='lessons')
    pos = models.PositiveSmallIntegerField(_('Position'))

    title = models.CharField(_('Title of Lesson'), max_length=256, unique=True)

    class Meta:
        unique_together = ('topic', 'pos')

    def __str__(self):
        return f'id={self.id}, pos={self.pos}, title="{self.title[:25]}"'


class Block(Publishable):
    lesson = CustomForeignKey(Lesson, verbose_name=_('Lesson'), related_name='blocks')
    pos = models.PositiveSmallIntegerField(_('Position'))

    title = models.CharField(_('Title of Block'), max_length=256, unique=True)
    text = models.TextField(_('Text of Block'))

    def __str__(self):
        return f'id={self.id}, title="{self.title[:25]}"'
