from django.conf.urls.defaults import *
from satchmo_store.urls import urlpatterns
from django.contrib import admin
from foa_store.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
