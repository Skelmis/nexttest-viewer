from typing import List

from django.http import HttpRequest
from django.shortcuts import render

from base.models import Repo, Entry
from base.utils import check_safe_redirect


def repo_view(request: HttpRequest, repo_slug: str):
    context = {"all_routes": []}
    try:
        all_entries: List[Entry] = Entry.objects.filter(repo__slug=repo_slug)
        raw_entries = []
        for entry in all_entries:
            redirect_url = request.get_full_path() + "/" + entry.slug
            if check_safe_redirect(request, redirect_url):
                raw_entries.append(redirect_url)

        context["all_routes"] = raw_entries
    except Repo.DoesNotExist:
        pass

    return render(request, "base/redirect.html", context=context)
