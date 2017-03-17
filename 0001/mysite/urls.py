from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'report/$', views.Report.as_view(), name='report'),
    url(r'report/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$',
        views.ReportDetails.as_view(), name='report_details'),
]
