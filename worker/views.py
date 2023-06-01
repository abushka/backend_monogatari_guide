from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import SerieSerializer, SerieStatusSerializer
from .models import Serie, SerieStatus

@api_view(['GET', 'POST'])  # Allow both GET and POST methods
def series_view(request):
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Logic for handling POST request, if needed
        # ...
        return Response('This is a POST request')  # Return appropriate response

    else:
        return Response({'detail': 'Method not allowed.'}, status=405)  # Return a "Method not allowed" response for unsupported methods


@api_view(['GET'])
def series_status_view(request):
    if request.method == 'GET':
        user = request.user  # Assuming you are using authentication and the user is available in the request
        series = Serie.objects.all()
        series_statuses = SerieStatus.objects.filter(user=user, serie__in=series)
        
        response_data = {}
        
        for serie in series:
            status = next((status for status in series_statuses if status.serie == serie), None)
            if status is None:
                # Если статус не найден, добавляем серию со статусом "не просмотрено"
                data = {
                    'serie': SerieSerializer(serie).data,
                    'status': 'not-watched'
                }
            else:
                # Если статус найден, добавляем серию и его статус
                data = {
                    'serie': SerieSerializer(serie).data,
                    'status': status.status
                }
                
            response_data[serie.id] = data
        
        if response_data:
            return Response(response_data)
        else:
            response_data = {
                'detail': 'У вас нет просмотренных серий.',
                'detail_en': 'You have no watched series.'
            }
            return Response(response_data, status=204)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)