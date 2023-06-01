from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SerieSerializer, ChapterSerializer
from .models import Serie, SerieStatus, Chapter, ChapterStatus

# Series
@api_view(['GET'])
def series_view(request):
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)

    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def series_status_view(request):
    if request.method == 'GET':
        user = request.user
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
                
            response_data[serie.number] = data
        
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
    
#Chapter
@api_view(['GET'])
def chapters_view(request):
    if request.method == 'GET':
        chapters = Chapter.objects.all()
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)

    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def chapters_status_view(request):
    if request.method == 'GET':
        user = request.user
        chapters = Chapter.objects.all()
        chapters_statuses = ChapterStatus.objects.filter(user=user, chapter__in=chapters)
        
        response_data = {}
        
        for chapter in chapters:
            status = next((status for status in chapters_statuses if status.chapter == chapter), None)
            if status is None:
                # Если статус не найден, добавляем серию со статусом "не просмотрено"
                data = {
                    'chapter': ChapterSerializer(chapter).data,
                    'status': 'not-watched'
                }
            else:
                # Если статус найден, добавляем серию и его статус
                data = {
                    'chapter': ChapterSerializer(chapter).data,
                    'status': status.status
                }
                
            response_data[chapter.number] = data
        
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