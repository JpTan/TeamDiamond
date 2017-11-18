from django.conf.urls import url
from . import views


urlpatterns = [
       url(r'^login/', views.user_login, name='login_url'),
       url(r'^signup/', views.user_signup, name='signup_url'),
]
