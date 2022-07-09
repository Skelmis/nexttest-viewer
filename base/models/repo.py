from django.db import models
from django.utils.text import slugify


class Repo(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=250, help_text="The name of this repo")
    link = models.URLField(help_text="A link to the Github repo")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Repo(slug='{self.slug}')"
