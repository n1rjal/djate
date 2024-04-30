from django.db import models
from django.core.cache import cache


class CachedModelManager(models.Manager):
    def cache_queryset(self, queryset):
        queryset_key = hash(queryset.query)
        queryset = cache.get(queryset_key)

        if queryset is None:
            queryset = super().get_queryset()
            cache.set(queryset_key, queryset, timeout=60)

        return cache.get(queryset_key)
