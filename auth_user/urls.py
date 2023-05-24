"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.views.generic import TemplateView
# from .views import SocialLoginView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    # path('rest-auth/social/login/', SocialLoginView.as_view(), name='social_login'),
]
