from django.conf.urls import url
from . import views

app_name = 'oas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^applicants/$', views.view_applicants, name='view_applicants'),
    url(r'^applicants/(?P<idnum>[0-9]{8})/$', views.view_applicant_detail, name='view_applicant_detail'),
    url(r'^applicants/(?P<idnum>[0-9]{8})/delete/$', views.delete_student, name='delete_student'),
    url(r'^applicants/(?P<idnum>[0-9]{8})/approve/$', views.approve_loan, name='approve_loan'),
    url(r'^applicants/(?P<idnum>[0-9]{8})/reject/$', views.reject_loan, name='reject_loan'),
    url(r'^loaners/$', views.view_loaners, name='view_loaners'),
    url(r'^loaners/(?P<idnum>[0-9]{8})/$', views.view_loaner_detail, name='view_loaner_detail'),
    url(r'^payments/pending/$', views.view_payments_pending, name='pending_payments'),
    url(r'^payments/all/$', views.view_payments_all, name='all_payments'),
    url(r'^payments/(?P<ornum>[\w{}.-]{1,20})/$', views.view_payment_detail, name='view_payment_detail'),
    url(r'^payments/(?P<ornum>[\w{}.-]{1,20})/approve$', views.approve_payment, name='approve_payment'),
    url(r'^payments/(?P<ornum>[\w{}.-]{1,20})/reject$', views.reject_payment, name='reject_payment'),
    url(r'^payments/(?P<ornum>[\w{}.-]{1,20})/edit$', views.edit_payment, name='edit_payment'),

]
