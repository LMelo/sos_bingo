from django.conf.urls import patterns, include, url
from bingo.views import bingo, index, cards

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bingo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="index"),
    url(r'^bingo/$', bingo, name="bingo"),
    url(r'^cards/$', cards, name="cards"),
)
