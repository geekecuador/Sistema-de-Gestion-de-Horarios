from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout

urlpatterns = [
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
	url(r'^accounts/logout/$', logout),
    url(r'^usuario/registro.html/$', ),


]
