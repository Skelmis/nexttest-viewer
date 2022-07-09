from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from base.models import Entry


@xframe_options_exempt
def entry_view(request: HttpRequest, repo_slug: str, entry_slug: str):
    try:
        entry: Entry = Entry.objects.get(slug=entry_slug, repo__slug=repo_slug)
    except Entry.DoesNotExist:
        raise 404

    return render(request, "base/entry.html", context={"entry": entry})
