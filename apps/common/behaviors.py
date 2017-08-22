from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import PublishableQuerySet


class Publishable(models.Model):
    publish_date = models.DateTimeField(_('Publish date'), null=True, blank=True, default=timezone.now)

    class Meta:
        abstract = True

    objects = PublishableQuerySet.as_manager()

    def publish_on(self, date=None):
        if not date:
            date = timezone.now()
        self.publish_date = date
        self.save()

    @property
    def is_published(self):
        return self.publish_date < timezone.now()
