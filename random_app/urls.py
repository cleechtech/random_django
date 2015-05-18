from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'random_app.views.home', name='home'),
]