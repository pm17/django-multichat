from django.conf.urls import url, include
from coordinator import views
from dashboard import urls as dashboard_urls


urlpatterns = [
	url(r'^$', views.main_panel, name='coord_main_panel'),
	# url(r'^(?P<event_id>\d+)/dashboard/$', views.dashboard, name='coord_dashboard')
]
