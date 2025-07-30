from django.db import models
from django.utils.text import slugify


class News(models.Model):
    slug     = models.SlugField(unique=True, blank=True)
    title    = models.CharField(max_length=250)
    summary  = models.TextField(blank=True)         # short teaser (home page)
    content  = models.TextField()                   # full article / release
    pub_date = models.DateField()

    class Meta:
        ordering = ["-pub_date"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pub_date:%Y-%m-%d} – {self.title}"