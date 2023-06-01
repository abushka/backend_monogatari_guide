from rest_framework_simplejwt.authentication import JWTAuthentication
from auth_user.models import CustomUser
from django.utils.functional import SimpleLazyObject

def get_user(request):
    user = None
    auth = JWTAuthentication()
    auth_header = auth.get_header(request)
    if auth_header:
        try:
            validated_token = auth.get_validated_token(auth_header)
            user_id = validated_token['user_id']
            User = CustomUser
            user = User.objects.get(pk=user_id)
        except:
            pass
    return user

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))
        response = self.get_response(request)
        return response