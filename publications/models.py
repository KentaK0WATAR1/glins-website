# publications/models.py
from django.db import models
from django.utils.text import slugify

class Publication(models.Model):
    slug    = models.SlugField(unique=True, blank=True)
    title   = models.CharField(max_length=255)
    authors = models.CharField(max_length=500)
    year    = models.PositiveSmallIntegerField()
    type    = models.CharField(max_length=50, blank=True)       # “Journal article” など
    doi     = models.CharField(max_length=100, blank=True)
    pdf     = models.URLField(blank=True)

    class Meta:
        ordering = ["-year", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            # タイトルから自動で slug を生成
            self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.year} – {self.title}"