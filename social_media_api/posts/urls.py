from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'likes', views.LikeViewSet, basename='likes')
router.register(r'unlikes', views.UnlikeViewSet, basename='unlikes')

urlpatterns = [
    path('post-data/', views.postData, name='post-data'),
    path('create-post/', views.createPost, name='create-post'),
    path('comment-data/', views.commentData, name='comment-data'),
    path('', include(router.urls)),
    path('feed/', views.FeedView.as_view(), name='feed'),
]