from django.urls import path,url
from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    url(r'^like/(\d+)',views.likePost, name="likePost"),
    url('about/', views.about, name="insta-about"),
    url('', PostListView.as_view(), name='insta-home'),
    url('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]