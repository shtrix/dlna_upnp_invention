from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, databrowse
import dlnaupnpmanagment
from django.views.generic.simple import direct_to_template
from django.conf import settings
from dlnaupnpmanagment import dlnaupnpmanage
from django.views.generic import list_detail
from django.views.generic.simple import redirect_to
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
 #  url('', RedirectView.as_view(url='/dlnaupnpmanagment/status'), name='some_redirect'),
    url(r'^dlnaupnpmanagment/index', direct_to_template, {'template': 'dlnaupnpmanage/index.html'}),
    url(r'^dlnaupnpmanagment/$', redirect_to, {'url': '/dlnaupnpmanagment/status'}),
    url(r'^dlnaupnpmanagment/status', 'dlnaupnpmanagment.dlnaupnpmanage.views.index'),
    url(r'^dlnaupnpmanagment/media', 'dlnaupnpmanagment.dlnaupnpmanage.views.media'),
    url(r'^dlnaupnpmanagment/serverstatus', 'dlnaupnpmanagment.dlnaupnpmanage.views.serverstatus'),
    url(r'^dlnaupnpmanagment/upnpserverstatus', 'dlnaupnpmanagment.dlnaupnpmanage.views.upnpserverstatus'),
    url(r'^dlnaupnpmanagment/settings', 'dlnaupnpmanagment.dlnaupnpmanage.views.settings'),
    url(r'^dlnaupnpmanagment/setname', 'dlnaupnpmanagment.dlnaupnpmanage.views.setname'),
    url(r'^dlnaupnpmanagment/update', 'dlnaupnpmanagment.dlnaupnpmanage.views.update'),
    url(r'^dlnaupnpmanagment/runserver', 'dlnaupnpmanagment.dlnaupnpmanage.views.runserver'),
    url(r'^dlnaupnpmanagment/stopserver', 'dlnaupnpmanagment.dlnaupnpmanage.views.stopserver'),
    url(r'^dlnaupnpmanagment/checkAddress', 'dlnaupnpmanagment.dlnaupnpmanage.views.checkAddress'),
    url(r'^dlnaupnpmanagment/getuuid', 'dlnaupnpmanagment.dlnaupnpmanage.views.getuuid'),
    url(r'^dlnaupnpmanagment/addContent', 'dlnaupnpmanagment.dlnaupnpmanage.views.addContent'),
    url(r'^dlnaupnpmanagment/saveSettings', 'dlnaupnpmanagment.dlnaupnpmanage.views.saveSettings'),
    url(r'^dlnaupnpmanagment/logs', 'dlnaupnpmanagment.dlnaupnpmanage.views.logs'),
    (r'^databrowse/(.*)', databrowse.site.root),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)