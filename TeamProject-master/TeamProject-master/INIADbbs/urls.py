from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index,name='index'),
        url(r'^create/$',views.create, name='create'),
        url(r'^edit/(?P<editing_id>\d+)/$',views.edit, name='edit'),
        url(r'^delete/$',views.delete, name='delete'),
]
