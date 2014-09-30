from django.conf.urls import patterns, url 
from hw import views

urlpatterns = patterns( 'hw.views', 
	url(r'^$', views.index, name='index'), 
	url(r'^about', views.about, name='about'),
	url(r'^better/$',views.better, name='betterhello')
	)
