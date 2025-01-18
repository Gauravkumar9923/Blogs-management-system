from django.urls import path
from blogs_management import blogs_api

urlpatterns = [
    path("posts/create-posts", blogs_api.create_blogs, name="create_posts"),
    path("posts/get-posts", blogs_api.get_blogs, name="get_all_posts"),
    path("posts/get-posts-by-id", blogs_api.get_blogs_by_id, name="get_posts_by_id"),
    path("posts/update-posts", blogs_api.update_blogs, name="update_blogs"),
    path("posts/delete-posts", blogs_api.delete_blogs, name="delete_blogs"),
    path("posts/delete-posts", blogs_api.like_dislike_posts, name="like_dislike_posts"),
    path("posts/delete-posts", blogs_api.add_comment_on_posts, name="add_comment_on_posts"),
    path("posts/delete-posts", blogs_api.get_blogs, name="get_blogs"),
]