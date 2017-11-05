from django.conf.urls import url
from django.contrib.auth import views as auth_views
app_name = 'student'
from . import views as student_views

urlpatterns = [
    url(r'^$', student_views.index, name='index'),
    url(r'^signup/$', student_views.signup, name='signup'),
    url(r'^login/$', student_views.login, name='login'),
    url(r'^logout/$', student_views.logout, name='logout'),
]
