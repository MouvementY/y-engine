from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views import generic

from core.views import ExtraContextTemplateView


urlpatterns = patterns('',
    url(r'^api/', include('apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.LOADERIO_ENABLED:
    token = settings.LOADERIO_TOKEN
    urlpatterns += patterns('',
        url(r'^loaderio-{}\.txt$'.format(token),
            ExtraContextTemplateView.as_view(template_name="services/loaderio.txt",
                                             extra_context={"token": token})),
    )


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
