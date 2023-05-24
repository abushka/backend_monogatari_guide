from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import CustomUser

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
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