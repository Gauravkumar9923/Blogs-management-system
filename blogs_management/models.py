from django.db import models
from uuid import uuid4
from accounts.models import Users

# Create your models here.
class Posts(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=36, default=uuid4)
    accounts = models.ForeignKey(Users,on_delete=models.CASCADE)
    user_posts = models.TextField()
    post_like_counter = models.IntegerField(default=0)
    post_unlike_counter = models.IntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_posts(cls,**kwargs):
        obj = cls(**kwargs)
        obj.save()
        return obj


class Comments(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=36, default=uuid4)
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="user_posts_mapping")
    comments = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now_add=True)


