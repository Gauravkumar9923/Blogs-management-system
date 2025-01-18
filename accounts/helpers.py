
import random
import string

ROLE_CHOICES = (
    ('author','Author'),
    ('reader', 'Reader')
)
def get_unique_random_string():
    from accounts.models import Users
    """
    It would generate unique random id for model field.
    :return:
    """
    random_num = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    while(True):
        if Users.objects.filter(account_number=random_num).exists():
            random_num = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        else: break
    return random_num

