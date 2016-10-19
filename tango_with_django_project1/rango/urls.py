from django.conf.urls import patterns, url
from rango import views
from django.conf.urls import include
from django.contrib import admin



urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^anubhav/', views.psycho, name='index2'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^about/$', views.about, name='about'),
        url(r'^search/$', views.search, name='search'),
        url(r'^goto$', views.track_url, name= 'goto'),
        url(r'^like_category/$', views.like_category, name='like_category'),
        url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
        url(r'^accounts/', include('registration.backends.simple.urls')))

"""urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    )"""