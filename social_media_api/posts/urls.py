from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'likes', views.LikeViewSet)

urlpatterns = [
    #path('posts-details/', views.postData, name='posts'),
    #path('create-post/', views.createPost, name='create-post'),
    #path('comments-details/', views.commentData, name='comments'),
    path('', include(router.urls)),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('post/<int:pk>/like/', views.LikeViewSet.as_view({'post':'like'}), name='post-like'),
    path('post/<int:pk>/unlike/', views.UnlikeViewSet.as_view({'post':'unlike'}), name='post-unlike'),
]