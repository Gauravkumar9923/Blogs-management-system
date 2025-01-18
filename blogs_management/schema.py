from marshmallow import (
    Schema,
    fields,
    validates,
    ValidationError,
    validates_schema,
    post_load,
    validate,
    post_dump,
    pre_load,
)
from blogs_management.models import Posts,Comments
from django.core.exceptions import ValidationError

class UserPostSchema(Schema):
    model = Posts
    id = fields.UUID(dump_only=True)
    user_posts = fields.String()
    account_id = fields.UUID(dump_only=True)

class UserPostLikeDislikeSchema(Schema):
    model = Posts
    post_like_counter = fields.Boolean(required=False)
    post_unlike_counter = fields.Boolean(required=False)

    @post_load
    def validate_data(self,data):
        if not data.get("post_like_counter",None) and not data.get("post_unlike_counter",None):
            raise ValidationError("either post_like counter or post_unlike_counter is required.")
        return data

class AddCommentSchema(Schema):
    model=Comments
    comments = fields.Str(required=True)
    





    
