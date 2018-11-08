from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import PostCreateView, PostUpdateView, PostDeleteView, PostListView, PostDetailView

app_name = 'main_app'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('add/', PostCreateView.as_view(), name='add_post'),
    path('edit/<int:pk>/', login_required(PostUpdateView.as_view()), name='edit_post'),
    path('delete/<int:pk>/', login_required(PostDeleteView.as_view()), name='delete_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    ]