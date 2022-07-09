from django.contrib import admin

from base.models import Repo, Entry


@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "link")


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("slug", "repo_name", "created_at", "last_edited_at")
    list_filter = ("repo",)

    def repo_name(self, obj):
        return obj.repo.name
