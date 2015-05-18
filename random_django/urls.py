from django.conf.urls import patterns, include, url
from django.contrib import admin
from random_app import urls as random_urls

urlpatterns = patterns('',

	url(r'^', include(random_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
