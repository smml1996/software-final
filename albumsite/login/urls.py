from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^signup/$',views.signup, name="registro"),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^$',auth_views.login,{'template_name': 'index.html'}, name="index"),
]
