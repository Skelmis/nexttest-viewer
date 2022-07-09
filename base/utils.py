from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme


def check_safe_redirect(request, uri):
    if not url_has_allowed_host_and_scheme(
        url=uri,
        allowed_hosts=settings.ALLOWED_HOSTS,
        require_https=request.is_secure(),
    ):
        return False

    return True
