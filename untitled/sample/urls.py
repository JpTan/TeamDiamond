"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
app_name = 'sample'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^view_status/$', views.view_status, name='view_status'),
    url(r'^payment/add/$', views.PaymentCreate.as_view(), name='payment-add'),
    url(r'^view_payments/$', views.PaymentLView.as_view(), name='view_payments'),
    url(r'^view_payment_details/(?P<pk>[a-zA-Z0-9]*)/$', views.PaymentDView.as_view(), name='view_payment_details'),
    url(r'^calculator/$', views.loan_calc, name='calculator'),
    url(r'^calculator/result/$', views.loan_calc, name='result'),
    url(r'^calculator/loan_projection/$', views.loan_projection, name='loan_projection'),
    url(r'^calculator/loan_projection/view$', views.loan_projection, name='projection_result'),
]