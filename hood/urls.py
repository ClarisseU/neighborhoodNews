from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^<id>/business/$', views.business, name="new-business"),
    url(r'^neighborhood$',views.neighborhood,name='neighborhood'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/newprofile$',views.new_profile, name ='new-profile'),
    url(r'^new/profile$',views.profile, name ='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)