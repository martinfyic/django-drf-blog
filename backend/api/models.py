from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    categories = models.ManyToManyField('Category')
    feature = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
