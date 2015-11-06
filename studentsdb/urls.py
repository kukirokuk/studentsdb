
from django.conf.urls import include, url, patterns
from django.contrib import admin
from students.views.students import StudentUpdateView, StudentDeleteView, StudentCreateView
from students.views.groups import GroupCreateView, GroupUpdateView
from students.views.contact_admin import CustomContactFormView

urlpatterns = [
	#Journal urls
	url(r'journal$', 'students.views.journal.journal', name='journal'),
	#Students urls
	url(r'^$', 'students.views.students.students_list', name='home'),
	url(r'students/add/$', StudentCreateView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',StudentUpdateView.as_view(), name='students_edit'),	
    url(r'^students/(?P<pk>\d+)/delete/$',StudentDeleteView.as_view(), name='students_delete'),

	#Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', GroupCreateView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(),
         name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete',
         name='groups_delete'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^contact-admin/', CustomContactFormView.as_view(), name='contact_form'),


    ]

from .settings import MEDIA_ROOT, DEBUG


if DEBUG:
# serve files from media folder
		urlpatterns += patterns('',
				url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
						'document_root': MEDIA_ROOT}))
