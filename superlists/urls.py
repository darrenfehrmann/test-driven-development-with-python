from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'lists.views.home_page', name='home'),
]
