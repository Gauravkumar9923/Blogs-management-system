from blogs_management.models import Posts , Comments
from django.views.decorators.http import require_http_methods
from blogs_management.schema import UserPostSchema, UserPostLikeDislikeSchema, AddCommentSchema
from accounts import exceptions
from django.http import JsonResponse
import datetime

@require_http_methods(["Post"])
def create_blogs(request,*args,**kwargs):
    model = Posts
    schema = UserPostSchema
    message = "Blog successfully created."
    data, error = schema.loads(request.body)
    if error:
        raise exceptions.BadRequestData(errors=error)
    try :
        inst=model.objects.create(**data)
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    return JsonResponse(
        { "id":inst.id},
        status=201,
        )

@require_http_methods(["Delete"])
def delete_blogs(request,*args,**kwargs):
    model = Posts
    schema = UserPostSchema
    message = "Blog successfully deleted."
    try :
        id = None
        model.objects.delete(id=id)
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    return JsonResponse(
        {},
        status=200,
        )

@require_http_methods(["Get"])
def get_blogs(request,*args,**kwargs):
    model = Posts
    schema = UserPostSchema
    message = "Blog successfully created."
    data, error = schema.loads(request.body)
    if error:
        raise exceptions.BadRequestData(errors=error)
    try :
        registration_number=request.GET.get("registration_number")
        queryset=model.objects.filter(account__account_number=registration_number)
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    response_dict=dict()
    payload = list()
    for item in queryset:
        append_dict={
            "id":item.id,
            "user_post":item.user_post,
            "post_like_counter":item.post_like_counter,
            "post_unlike_counter":item.post_unlike_counter,
            "created_timestamp":item.created_timestamp,
            "update_timestamp":item.update_timestamp
        }
        payload.append(append_dict)
        response_dict["message"]=message
        response_dict["payload"]=payload
        
    return JsonResponse(
        response_dict,
        status=202,
        )

@require_http_methods(["Get"])
def get_blogs_by_id(request,*args,**kwargs):
    model = Posts
    schema = UserPostSchema
    message = "Blog successfully created."
    data, error = schema.loads(request.body)
    if error:
        raise exceptions.BadRequestData(errors=error)
    try :
        post_id=request.GET.get("post_id")
        qs=model.objects.get(id=post_id)
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    response_dict=dict()
    payload = list()
    
    append_dict={
        "id":qs.id,
        "user_post":qs.user_post,
        "post_like_counter":qs.post_like_counter,
        "post_unlike_counter":qs.post_unlike_counter,
        "created_timestamp":qs.created_timestamp,
        "update_timestamp":qs.update_timestamp
    }
    payload.append(append_dict)
    response_dict["message"]=message
    response_dict["payload"]=payload
        
    return JsonResponse(
        response_dict,
        status=202,
        )

@require_http_methods(["Post"])
def update_blogs(request,*args,**kwargs):
    model = Posts
    schema = UserPostSchema
    message = "Blog successfully created."
    data, error = schema.loads(request.body)
    if error:
        raise exceptions.BadRequestData(errors=error)
    try :
        post_id=request.GET.get("post_id")
        model_inst = Posts.objects.filter()
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    return JsonResponse(
        { "id":model_inst.id},
        status=201,
        )

@require_http_methods(["Post"])
def like_dislike_posts(request,*args,**kwargs):
    model = Posts
    schema = UserPostLikeDislikeSchema
    message = "response successfully captured."
    data, error = schema.loads(request.body)
    if error:
        raise exceptions.BadRequestData(errors=error)
    try :
        post_id=request.GET.get("post_id")
        model_inst = Posts.objects.filter(id=post_id)
        model_inst.update(**data,update_ts=datetime.datetime.now())
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    return JsonResponse(
        { "id":model_inst.id},
        status=201,
        )

@require_http_methods(["Post"])
def add_comment_on_posts(request,*args,**kwargs):
    model = Posts
    schema = AddCommentSchema
    message = "response successfully captured."
    data, error = schema.loads(request.body)
    if error:
        raise exceptions.BadRequestData(errors=error)
    try :
        post_id=request.GET.get("post_id")
        model_inst = Posts.objects.filter(id=post_id)
        Comments.objects.create(post=model_inst,**data)
        model_inst.update(**data,update_ts=datetime.datetime.now())
    except Exception as e:
        raise exceptions.BadRequestData(errors=str(e))
    return JsonResponse(
        { "id":model_inst.id},
        status=201,
        )