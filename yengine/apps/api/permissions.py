from rest_framework import permissions
from ipware.ip import get_real_ip

from .models import Blacklist


class BlacklistPermission(permissions.BasePermission):
    """
    Permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = get_real_ip(request)
        if ip_addr is None:
            return True

        blacklist_queryset = Blacklist.objects.filter(ip_address=ip_addr)

        # enable readonly state for safe requests
        safe_method = bool(request.method in permissions.SAFE_METHODS)
        if safe_method:
            blacklist_queryset = blacklist_queryset.filter(readonly=False)

        blacklisted = blacklist_queryset.exists()
        return not blacklisted
