from django.urls import path
from . import views, views_FBV
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views_FBV.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views_FBV.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views_FBV.post_detail, name='post_detail'),  # SEO url
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views_FBV.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views_FBV.post_search, name='post_search'),
]
