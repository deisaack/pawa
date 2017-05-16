from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from mzito.activities import views as activities_views
from mzito.authentication import views as mzito_auth_views
from mzito.core import views as core_views
from mzito.search import views as search_views
from . import views
from django.contrib import admin
from mzito.authentication import urls as prof_url
from mzito.apply import urls as apply_urls
from mzito.operation import urls as orp_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^gallery/$', views.GalleryPage.as_view(), name='gallery'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    # url(r'^login/$', auth_views.login, {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', mzito_auth_views.signup, name='signup'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture, name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture, name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^feeds/', include('mzito.feeds.urls')),
    url(r'^messages/', include('mzito.messenger.urls')),
    url(r'^notifications/$', activities_views.notifications, name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications, name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications, name='check_notifications'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^u/(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    url(r'^users/', include(prof_url, namespace='profiles')),
    url(r'^op/', include(orp_urls, namespace='operation')),
    url(r'^apply/', include(apply_urls, namespace='apply')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
