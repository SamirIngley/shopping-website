from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [

    path('', PostListView.as_view(), name='post-list-page'),
    path('new/', PostCreateView.as_view(), name='post-create-page'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail-page'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update-page'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete-page'),

]