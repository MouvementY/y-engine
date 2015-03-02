from django.conf.urls import patterns, url, include

from .routers import SecuredDefaultRouter
from .views import (
    SignatureViewSet,
    SubscribeToEventNotificationsView,
    PostViewSet)


signature_list = SignatureViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
signature_timeseries = SignatureViewSet.as_view({
    'get': 'timeseries',
})
post_list = PostViewSet.as_view({
    'get': 'list',
})

urlpatterns = patterns('',
    url(r'^signatures/$', signature_list, name='signature-list'),
    url(r'^signatures/timeseries/$', signature_timeseries, name='signature-timeseries'),
    url(r'^events/subscribe/$', SubscribeToEventNotificationsView.as_view()),
    url(r'^news/$', post_list, name='post-list'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
