from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import CustomUser
from allauth.socialaccount.models import SocialToken

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        # Вызов родительского метода для обработки перенаправления
        super().pre_social_login(request, sociallogin)
        
        # Проверка, что провайдер - Google
        if sociallogin.account.provider == 'google':
            # Получение токена доступа Google
            access_token = sociallogin.account.extra_data.get('access_token')
            
            # Сохранение токена в модели SocialToken
            if access_token:
                token, created = SocialToken.objects.get_or_create(
                    account=sociallogin.account,
                    token=access_token,
                )

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form=form)
        if user.username == 'user':
            new_username = sociallogin.account.extra_data.get('name')
            existing_user = CustomUser.objects.filter(username=new_username).first()
            if existing_user:
                new_username += str(sociallogin.account.extra_data.get('id'))
            user.username = new_username
            user.github_account = sociallogin.account.extra_data.get('html_url')
            user.save()
        return user