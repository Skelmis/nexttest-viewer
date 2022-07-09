from typing import List

from django.http import HttpRequest
from django.shortcuts import render

from base.models import Repo
from base.utils import check_safe_redirect


def index_view(request: HttpRequest):
    context = {"all_routes": []}
    try:
        all_entries: List[Repo] = Repo.objects.all()
        raw_entries = []
        for repo in all_entries:
            redirect_url = request.get_full_path() + repo.slug
            if check_safe_redirect(request, redirect_url):
                raw_entries.append([redirect_url])

        context["all_routes"] = raw_entries
    except Repo.DoesNotExist:
        pass
    return render(request, "base/redirect.html", context=context)
