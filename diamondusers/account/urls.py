from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^login/', views.user_login, name='login_url'),
       url(r'^signup/', views.user_signup, name='signup_url'),
       url(r'^logout/', views.user_logout, name='logout_url'),
       url(r'^(?P<pk>[0-9]+)/$', views.home_view.as_view(), name='home_url'),
]
