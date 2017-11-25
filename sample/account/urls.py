from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='Login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
