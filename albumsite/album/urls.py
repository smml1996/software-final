from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^album-virtual/$',views.album, name="albumpersonal"),
	url(r'^por-codigo/$',views.getPorCodigo, name="masFiguras"),


	url(r'^$',views.home, name="home"),
	url(r'^ajax/peticion_intercambio/$', views.peticionIntercambio, name='cambiape'),
]
