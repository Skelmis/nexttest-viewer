from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from base.models import Repo


class Entry(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(
        help_text="A description to display on the page", blank=True
    )
    log_file = models.FileField(upload_to="base/", help_text="The pytest HTML log file")
    test_file = models.URLField(help_text="A link to the actual test cases.")
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)

    def clean(self):
        if not self.log_file.name.endswith(".html"):
            raise ValidationError("Html files only")

    def __str__(self):
        return f"Entry(slug='{self.slug}', repo='{self.repo}')"

    class Meta:
        unique_together = ["repo", "slug"]
