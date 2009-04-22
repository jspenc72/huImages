from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^upload/', 'huimages.imagebrowser.views.upload'),
    (r'^image/random/', 'huimages.imagebrowser.views.random_image'),
    (r'^image/(?P<imageid>.+)/previous/', 'huimages.imagebrowser.views.previous_image'),
    (r'^image/(?P<imageid>.+)/next/', 'huimages.imagebrowser.views.next_image'),
    (r'^image/(?P<imageid>.+)/rate/', 'huimages.imagebrowser.views.rate'),
    (r'^image/(?P<imageid>.+)/favorite/', 'huimages.imagebrowser.views.favorite'),
    (r'^image/(?P<imageid>.+)/tag/', 'huimages.imagebrowser.views.tag'),
    (r'^image/(?P<imageid>.+)/update_title/', 'huimages.imagebrowser.views.update_title'),
    (r'^image/(?P<imageid>.+)/tag_suggestion/', 'huimages.imagebrowser.views.tag_suggestion'),
    url(r'^image/(?P<imageid>.+)/', 'huimages.imagebrowser.views.image', name='view-image'),
    (r'^favorites/(?P<uid>.+)/$', 'huimages.imagebrowser.views.favorites'),
    (r'^favorites/$', 'huimages.imagebrowser.views.favorites_redirect'),
    (r'^tag/(?P<tagname>.+)/', 'huimages.imagebrowser.views.by_tag'),
    (r'^$', 'huimages.imagebrowser.views.startpage'),
)
