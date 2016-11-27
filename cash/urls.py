from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_activity$', views.NewActivity.as_view(), name='new_activity'),
    url(r'^activity_list$', views.ActivityList.as_view(), name='activity_list'),
]
