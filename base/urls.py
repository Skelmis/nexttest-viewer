from django.urls import path

from base.views import index_view

urlpatterns = [
    path("", index_view),
]
