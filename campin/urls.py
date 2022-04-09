from django.urls import path, include
from . import views

urlpatterns = [
    # GET localhost:8000/posts
    # POST localhost:8000/posts
    path('posts/', views.PostList.as_view(), name='post_list'),
    # PUT localhost:8000/posts/:id
    # DELETE localhost:8000/posts/:id
    path('posts/<int:pk>',
         views.PostDetail.as_view(), name='post_detail'),
    # GET localhost:8000/comments
    # POST localhost:8000/comments
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    # PUT localhost:8000/comments/:id
    # DELETE localhost:8000/comments/:id
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]
