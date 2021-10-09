from django.db import models

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    source = models.ForeignKey(
        Source, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    urlToImage = models.URLField(null=True, blank=True)
    publishedAt = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
