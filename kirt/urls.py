from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kirt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/', include('registration.urls')),
    url(r'^$','src.views.index'),
    url(r'^addworker/','src.views.addworker'),
    #url(r'^src/addadvance/','src.views.addadvance'),
    url(r'^ajaxdetails/','src.views.ajaxdetails'),
    url(r'^ajaxrequest/','src.views.ajaxrequest'),
    url(r'^ajaxrequestpaid/','src.views.ajaxrequestpaid'),
    url(r'^popupadvance/','src.views.popupadvance'),
    url(r'^ajaxpopupadvance/','src.views.ajaxpopupadvance'),
    url(r'^particulars/','src.views.particulars'),
    url(r'^return_advance/','src.views.return_advance'),
    url(r'^deleteworker/','src.views.deleteworker'),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Are these things needed after + ?


