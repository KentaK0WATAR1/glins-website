# publications/models.py
from django.db import models

class Publication(models.Model):
    slug    = models.SlugField(primary_key=True)
    title   = models.CharField(max_length=255)
    authors = models.CharField(max_length=500)
    year    = models.PositiveSmallIntegerField()
    type    = models.CharField(max_length=50)       # “Journal article” など
    doi     = models.CharField(max_length=100, blank=True)
    pdf     = models.URLField(blank=True)

    class Meta:
        ordering = ["-year", "title"]

    def __str__(self):
        return f"{self.year} – {self.title}"