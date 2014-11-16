from django.conf.urls import patterns, url, include

from .routers import SecuredDefaultRouter
from .views import (
    SignatureViewSet,
    SubscribeToEventNotificationsView)


router = SecuredDefaultRouter()
router.register(r'signatures', SignatureViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^events/subscribe/', SubscribeToEventNotificationsView.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
