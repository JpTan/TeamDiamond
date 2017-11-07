from django.conf.urls import url
from . import views
app_name = 'student'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^login_user/$', views.login_user,  name='login'),
    url(r'^logout_user/$', views.logout_user, name='logout'),
]
