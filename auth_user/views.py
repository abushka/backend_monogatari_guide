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