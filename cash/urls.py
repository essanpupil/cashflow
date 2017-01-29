from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new-activity$', views.NewActivity.as_view(), name='new_activity'),
    url(r'^activity-list$', views.ActivityList.as_view(), name='activity_list'),
]
