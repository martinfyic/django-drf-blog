from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    categories = models.ManyToManyField('Category')
    feature = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True, null=False, blank=False)
    thumbnail = models.URLField(null=True)

    class Meta:
        verbose_name_plural = 'blogs'
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['date_created']

    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return

    instance.slug = slugify(instance.title)


pre_save.connect(set_slug, sender=Blog)
