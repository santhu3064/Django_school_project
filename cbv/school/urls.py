from django.conf.urls import url

from school.views import SchoolListView, SchoolDetailView, SchoolCreateView,SchoolUpdateView,SchoolDeleteView,StudentCreateView,StudentUpdateView,StudentDeleteView

app_name = 'school'
urlpatterns = [
    url(r'^$', SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', SchoolDetailView.as_view(), name='detail'),
    url(r'^create/',SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', SchoolDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/add/student/$', StudentCreateView.as_view(), name='create_student'),
   url(r'^(?P<pk>\d+)/update/student/$', StudentUpdateView.as_view(), name='update_student'),
    url(r'^(?P<pk>\d+)/delete/student/$', StudentDeleteView.as_view(), name='delete_student'),
]
