from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [

    path('', PostListView.as_view(), name='post-list-page'),
    path('create/', PostCreateView.as_view(), name='post-create-page'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail-page'),

]