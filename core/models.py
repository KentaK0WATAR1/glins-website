from django.db import models
from django.utils.text import slugify


class TeamMember(models.Model):
    name       = models.CharField(max_length=120)
    position   = models.CharField(max_length=120, blank=True)
    affiliation = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name