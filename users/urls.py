from django.conf.urls import url
from insta.users import views as insta_views
from django.urls import path

urlpatterns = [
    # url(r'^signup/$', insta_views.signup, name='signup'),
    path('', views.index,name='index'),
]
