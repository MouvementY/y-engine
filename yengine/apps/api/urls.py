from django.conf.urls import patterns, url, include

from .routers import SecuredDefaultRouter
from .views import (
    SignatureViewSet,
    SubscribeToEventNotificationsView)


signature_list = SignatureViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = patterns('',
    url(r'^signatures/', signature_list, name='signature-list'),
    url(r'^events/subscribe/', SubscribeToEventNotificationsView.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
