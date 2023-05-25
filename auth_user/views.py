from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login
from dj_rest_auth.serializers import JWTSerializer
from dj_rest_auth.views import LoginView

@receiver(pre_social_login)
def create_jwt_token(sender, request, sociallogin, **kwargs):
    # Получение доступа к токену авторизации
    token = sociallogin.token

    # Создание JWT токена с использованием dj_rest_auth
    jwt_serializer = JWTSerializer()
    jwt_token = jwt_serializer.create_token(request.user)

    # Возврат JWT токена в ответе
    login_view = LoginView()
    response = login_view.get_response(request)
    response.data['token'] = jwt_token

    return response



# from dj_rest_auth.views import LoginView
# from rest_framework.authtoken.models import Token

# class SocialLoginView(LoginView):
#     def login(self):
#         self.user = self.serializer.validated_data['user']
#         token, _ = Token.objects.get_or_create(user=self.user)
#         response = {
#             'token': token.key,
#         }
#         return response