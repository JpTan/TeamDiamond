from django.conf.urls import url
from . import views

app_name="account"

urlpatterns = [
       url(r'^login/', views.user_login, name='login_url'),
       url(r'^signup/', views.user_signup, name='signup_url'),
       url(r'^logout/', views.user_logout, name='logout_url'),
       #url(r'^update/', views.user_update, name='update_url'),
       url(r'^(?P<pk>[0-9]+)/$', views.home_view.as_view(), name='home_url'),
]
