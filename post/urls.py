from django.urls import path
from post import views, models

urlpatterns = [
path('list/', views.PostsListView.as_view(), name='list'),
#path('<int:pk>/detail/', views.PostDetailView.as_view(), name='detail'),
path('<int:pk>/detail/', views.post_detail, name='detail'),
path('sc_list/', views.SciencePostsListView.as_view(), name='science_list'),
path('tch_list/', views.TechnologiesPostsListView.as_view(), name='technologies_list'),
path('search/', views.post_search, name='search'),
]