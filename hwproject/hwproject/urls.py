from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hwproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^%',views.index, name='index'),
   # url(r'^h/', include('hw.urls')),
    url(r'^',include('hw.urls')),
    url(r'^about/', include ('hw.urls'))
)
