from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser
from dj_rest_auth.views import UserDetailsView
from rest_framework import status


# Users
@api_view(['GET'])
def user_view(request):
    if request.method == 'GET':
        user = request.user
        CustomUsers = CustomUser.objects.all()
        Custom_user = CustomUsers.objects.filter(user=user)
        
        response_data = {}
        
        if Custom_user:
            
            data = {
                'user': CustomUserSerializer(Custom_user).data
            }
            return Response(data)
        else:
            response_data = {
                'detail': 'Нет такого пользователя.',
                'detail_en': 'This user is death.'
            }
            return Response(response_data, status=204)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)
    


# User change info
class CustomUserChange(UserDetailsView):
    def put(self, request, *args, **kwargs):
        # Получаем данные из запроса
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        image = request.FILES.get('image', None)

        # Получаем текущего пользователя
        user = request.user

        # Обновляем поля, если они переданы и отличаются от текущих значений
        if username is not None and username is not '' and username != user.username:
            user.username = username

        if email is not None and email is not '' and email != user.email:
            user.email = email

        if image is not None and image is not '':
            # Проверяем, чтобы image не был пустым
            if image:
                # Сохраняем путь к файлу фотографии в поле image пользователя
                user.image = image
                user.image_thumbnail = image

        # Сохраняем обновленного пользователя
        user.save()

        return Response({
            'username': user.username,
            'email': user.email,
            'profile_picture_url': user.image_url(request),
            "message": "Информация о пользователе обновлена"}, status=status.HTTP_200_OK)
    

# User language change
class CustomUserLanguageChange(UserDetailsView):
    def put(self, request, *args, **kwargs):
        
        language = request.data.get('language', 'ru')

        user = request.user

        if language is not None and language is not '' and language != user.language:
            user.language = language

        user.save()

        return Response({
            'language': user.language,
            "message": "Язык пользователя обновлён"}, status=status.HTTP_200_OK)
    

# Users
@api_view(['POST'])
def user_avatar_delete(request):
    if request.method == 'POST':
        user = request.user

        if user and user.image:
            user.image.delete(save=True)
            user.image_thumbnail.delete(save=True)
            return Response({"message": "Фото профиля удалено"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Фото профиля не найдено"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "Неверный метод запроса"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        