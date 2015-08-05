from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from srh import settings
from userprofile.views import Busqueda_info_ajax
urlpatterns = [
    # Examples:
    # url(r'^$', 'srh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^rank/$', 'userprofile.views.academirank',name='academirank'),
	url(r'^accounts/logout/$', logout),
    url(r'^login/','userprofile.views.login_user',name='login_user'),
    url(r'^(?:signin.html)?$','userprofile.views.login_user',name='login'),
    url(r'^logout/$', login),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^info_ajax/$',Busqueda_info_ajax.as_view()),

]
