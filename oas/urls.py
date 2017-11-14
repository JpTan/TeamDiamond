from django.conf.urls import url
from . import views

app_name = 'oas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^applicants/$', views.view_applicants, name='view_applicants'),
    url(r'^applicants/(?P<idnum>[0-9]{8})/$', views.view_applicant_detail, name='view_applicant_detail'),
    url(r'^applicants/delete_(?P<idnum>[0-9]{8})/$', views.delete_student, name='delete_student')
]
