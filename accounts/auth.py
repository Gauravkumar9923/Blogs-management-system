from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from accounts.models import Users,UserLogin
import json
from django.core.exceptions import ValidationError
from django.db.models import Q
from accounts.helpers import get_unique_random_string


@require_http_methods(["POST"])
def user_login(request):
    model=UserLogin
    data=json.loads(request.body)
    req_fields = {"username","password"}
    username=data.get("username")
    if req_fields != data.keys():
        raise ValidationError("either username or password is missing")
    try:
        is_account_exist=Users.objects.get(Q(mobile_number=username)|Q(email=username),password=data.get("password"))
        model.user_login(account=is_account_exist[0])
    except Users.DoesNotExist:
        raise ValidationError("User unable to login")

@require_http_methods(["POST"])
def create_accounts(request):
    data = json.loads(request.body)
    req_fields = ["name","first_name","last_name","mobile_number","email","account_number","password","role"]
    list2 = data.keys()
    data["account_number"] = get_unique_random_string()
    print("check")
    print("data ",data)
    if all(item in req_fields for item in list2) and len(data)==len(req_fields):

        obj = Users.register_user(**data)
    else:
        raise ValidationError("Unable to create account")
    print("check")
    return JsonResponse(
        {"account_number":obj.account_number,
          "name":obj.name},
                status=201,
            )

@require_http_methods(["GET"])
def get_account_details(request):

    mobile_number=request.GET.get("mobile_number")
    query=Users.objects.filter(mobile_number=mobile_number)
    response_dict={
        "account_number":query[0].account_number,
        "account_name":query[0].name,
        "email":query[0].email,
        "mobile_number":query[0].mobile_number,
        "first_name":query[0].first_name,
        "last_name":query[0].last_name
    }if query else {}
    return JsonResponse(
        response_dict,
        status=202
    )
    
