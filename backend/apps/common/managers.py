from django.db import models

from django.utils import timezone


class PublishableQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(publish_date__lte=timezone.now())
