from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.result, name='result'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^recalc/$', views.recalc, name='recalc'),
    url(r'^voting/$', views.voting, name='voting'),
]
