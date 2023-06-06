from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SerieSerializer, SeasonSerializer, ChapterSerializer, VolumeSerializer
from .models import Serie, SerieStatus, Season, SeasonStatus, Chapter, ChapterStatus, Volume, VolumeStatus

# Series
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def series_view(request):
    if request.method == 'GET':
        series = Serie.objects.all()

        # Создаем словарь серий с номерами в качестве ключей
        serialized_series = {}
        for serie in series:
            serialized_serie = SerieSerializer(serie).data
            serialized_serie['number'] = serie.number
            serialized_series[str(serie.number)] = serialized_serie

        return Response(serialized_series)
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
                serie_data = SerieSerializer(serie).data
                serie_data['status'] = 'not-watched'
            else:
                # Если статус найден, добавляем серию и её статус
                serie_data = SerieSerializer(serie).data
                serie_data['status'] = status.status

            response_data[serie.number] = {'serie': serie_data}

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


# Seasons
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def seasons_view(request):
    if request.method == 'GET':
        seasons = Season.objects.all()
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data)

    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def seasons_status_view(request):
    if request.method == 'GET':
        user = request.user
        seasons = Season.objects.all()
        seasons_statuses = SeasonStatus.objects.filter(user=user, season__in=seasons)

        response_data = {}

        for season in seasons:
            status = next((status for status in seasons_statuses if status.season == season), None)
            if status is None:
                # Если статус не найден, добавляем серию со статусом "не просмотрено"
                season_data = SeasonSerializer(season).data
                season_data['status'] = 'not-watched'
            else:
                # Если статус найден, добавляем серию и её статус
                season_data = SeasonSerializer(season).data
                season_data['status'] = status.status

            response_data[season.number] = {'season': season_data}

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
    

@api_view(['POST'])
def seasons_save_status_view(request):
    token = request.data.get('token')
    season_number = request.data.get('season_number')
    status = request.data.get('status')

    user = request.user

    try:
        season = Season.objects.get(number=season_number) 
    except Season.DoesNotExist:
        return Response({'detail': 'Season not found.'}, status=404)

    try:
        season_status = SeasonStatus.objects.get(user=user, season=season)
        season_status.status = status
        season_status.save()
    except SeasonStatus.DoesNotExist:
        season_status = SeasonStatus.objects.create(user=user, season=season, status=status)

    return Response({'detail': 'Status saved successfully.'})


#Chapter
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
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
    

# Volumes
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def volumes_view(request):
    if request.method == 'GET':
        volumes = Volume.objects.all()
        serializer = VolumeSerializer(volumes, many=True)
        return Response(serializer.data)

    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def volumes_status_view(request):
    if request.method == 'GET':
        user = request.user
        volumes = Volume.objects.all()
        volumes_statuses = VolumeStatus.objects.filter(user=user, volume__in=volumes)

        response_data = {}

        for volume in volumes:
            status = next((status for status in volumes_statuses if status.volume == volume), None)
            if status is None:
                # Если статус не найден, добавляем серию со статусом "не просмотрено"
                volume_data = VolumeSerializer(volume).data
                volume_data['status'] = 'not-watched'
            else:
                # Если статус найден, добавляем серию и её статус
                volume_data = VolumeSerializer(volume).data
                volume_data['status'] = status.status

            response_data[volume.number] = {'volume': volume_data}

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