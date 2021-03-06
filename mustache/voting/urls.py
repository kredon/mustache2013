from django.conf.urls import patterns, include, url

import voting.views

urlpatterns = patterns('',
    url(r'^participate$', voting.views.participate, name='participate'),
    url(r'^register$', voting.views.register, name='register'),
    url(r'^profile$', voting.views.profile, name='profile'),
    url(r'^comment$', voting.views.comment, name='comment'),
    url(r'^vote$', voting.views.vote, name='vote'),
    url(r'^login$', voting.views.login, name='login'),
    url(r'^logout$', voting.views.logout, name='logout'),
    url(r'^results$', voting.views.results, name='results'),
)
