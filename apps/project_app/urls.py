from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.items),
    url(r'^add$', views.add_item),
    url(r'^process_item$', views.process_item),
    url(r'^wish_items/(?P<item_id>\d+)$', views.wish_items),
    url(r'^join/(?P<item_id>\d+)$', views.join),
    url(r'^remove/(?P<item_id>\d+)$', views.remove),
    url(r'^delete/(?P<item_id>\d+)$', views.delete)
  ]
