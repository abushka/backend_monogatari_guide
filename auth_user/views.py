# facebook
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# twitter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer
# github
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

import urllib.parse

from django.shortcuts import redirect

# from django.urls import reverse
# google
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from dj_rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'https://abushka.uz:8000/api/auth/github/login/callback/'
    client_class = OAuth2Client

#     @property
#     def callback_url(self):
#         # use the same callback url as defined in your GitHub app, this url
#         # must be absolute:
#         return self.request.build_absolute_uri(reverse('github_callback'))
    
def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'https://abushka.uz:8000/auth/github?{params}')


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/api/auth/google/login/callback/'
    client_class = OAuth2Client

class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter