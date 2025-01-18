from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from blogs_management.models import Posts
from django.conf import settings

@shared_task
def send_welcome_mail(user_id):
    user=User.objects.get(id=user_id)
    send_mail(
        'Welcome!',
        'Thanks for registering!',
        'from@example.com',
        [user.email],
        fail_silently=False
    )

@shared_task
def generate_daily_stats():
    total_post_generated = Posts.objects.filter()
    send_mail(
        'Welcome!',
        'Thanks for registering!',
        'from@example.com',
        [settings.ADMIN_EMAIL],
        fail_silently=False
    )
