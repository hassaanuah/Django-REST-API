from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^firewall1/$', 'mysite.views.firewall1', name='firewall1'),
    url(r'^firewall/(?P<parameter>[\w|\W]+)=(?P<value>[\w|\W]+)/$', 'mysite.views.firewall', name='firewall'),
    url(r'^host/(?P<parameter>[\w|\W]+)=(?P<value>[\w|\W]+)/$', 'mysite.views.host', name='host'),
    url(r'^ces/transport_protocol=(?P<transport>[\w|\W]+)/link_alias=(?P<link>[\w|\W]+)/reputation=(?P<repute>[\w|\W]+)/$', 'mysite.views.ces', name='ces'),
    #url(r'^firewall/fqdn=(?P<fqdn>\w{0,50})/$', 'mysite.views.firewall', name='firewall'),
    #url(r'^(?P<file2delete>[\w|\W]+)/checking/(?P<id2delete>[\w|\W]+)$', 'uploader.views.listoriginal', name='listoriginal'),

]


'''
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'uploader.views.main', name='main'),
    url(r'^login/$', 'uploader.views.login', name='login'),
    url(r'^verify/$', 'uploader.views.verify', name='verify'),
    url(r'^list_videos/$', 'uploader.views.list_videos', name='list_videos'),
    url(r'^addvideo/$', 'uploader.views.addvideo', name='addvideo'),
    url(r'^cache/$', 'uploader.views.cache', name='cache'),
    url(r'^(?P<file2delete>[\w|\W]+)/checking/(?P<id2delete>[\w|\W]+)$', 'uploader.views.listoriginal', name='listoriginal'),
    url(r'^cdndatabase/$', 'uploader.views.cdndatabase', name='cdndatabase'),
    url(r'^logout/$', 'uploader.views.logout', name='logout'),
    url(r'^streamer/$', 'uploader.views.streamer', name='streamer'),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
