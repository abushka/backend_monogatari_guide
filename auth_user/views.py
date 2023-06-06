from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser

# class CustomUserView(RetrieveAPIView):
#     serializer_class = CustomUserSerializer

#     def get_object(self):
#         # Возвращает объект пользователя текущего запроса
#         return self.request.user
    
# Users
@api_view(['GET'])
def series_status_view(request):
    if request.method == 'GET':
        user = request.user
        CustomUsers = CustomUser.objects.all()
        Custom_user = CustomUsers.objects.filter(user=user)
        
        response_data = {}
        
        if Custom_user:
            # Если статус не найден, добавляем серию со статусом "не просмотрено"
            data = {
                'user': CustomUserSerializer(Custom_user).data
            }
        # else:
        #     # Если статус найден, добавляем серию и его статус
        #     data = {
        #         'serie': SerieSerializer(serie).data,
        #         'status': status.status
        #     }
            
            return Response(data)
        else:
            response_data = {
                'detail': 'Нет такого пользователя.',
                'detail_en': 'This user is death.'
            }
            return Response(response_data, status=204)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)