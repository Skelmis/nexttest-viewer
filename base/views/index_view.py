from django.http import HttpRequest
from django.shortcuts import render


def index_view(request: HttpRequest):
    context = {"all_routes": []}
    return render(request, "base/index.html", context=context)
