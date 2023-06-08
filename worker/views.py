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
    

@api_view(['POST'])
def series_save_status_view(request):
    serie_number = request.data.get('serie_number')
    status = request.data.get('status')

    user = request.user

    try:
        serie = Serie.objects.get(number=serie_number) 
    except Serie.DoesNotExist:
        return Response({'detail': 'Serie not found.'}, status=404)

    try:
        serie_status = SerieStatus.objects.get(user=user, serie=serie)
        serie_status.status = status
        serie_status.save()
    except SerieStatus.DoesNotExist:
        serie_status = SerieStatus.objects.create(user=user, serie=serie, status=status)

    return Response({'detail': 'Status saved successfully.'})


# Seasons
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def seasons_view(request):
    if request.method == 'GET':
        seasons = Season.objects.all()
        serialized_seasons = {}
        for season in seasons:
            serialized_season = SeasonSerializer(season).data
            serialized_season['number'] = season.number
            serialized_seasons[str(season.number)] = serialized_season
        # serializer = SeasonSerializer(seasons, many=True)
        return Response(serialized_seasons)

    else:
        return Response({'detail': 'Method not allowed.'}, status=405)

    #     for serie in series:
    #         serialized_serie = SerieSerializer(serie).data
    #         serialized_serie['number'] = serie.number
    #         serialized_series[str(serie.number)] = serialized_serie

    #     return Response(serialized_series)
    # else:
    #     return Response({'detail': 'Method not allowed.'}, status=405)


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
    

# сначала я должен создать переменную previous_serie = None, дальше должен идти цикл по полю anime_release_view_number у серий, в цикле я должен смотреть если previous_serie не равен None и сезон серии не такой же как previous_serie, то я должен добавлять сначала сезон, потом пихать серию в массив серий, если всё же previous_serie не равен None, но равен previous_serie, то я должен просто пихать серию в уже существующий массив серий 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def series_view(request):
    if request.method == 'GET':
        series = Serie.objects.all().order_by('anime_release_view_number')

        serialized_seasons = []
        serialized_seasons_dict = {}
        previous_season_id = None
        i = 1

        for serie in series:
            current_season_id = serie.season.id

            if current_season_id != previous_season_id:
                season = Season.objects.filter(id=current_season_id).first()
                serialized_season = SeasonSerializer(season).data
                serialized_season['series'] = []

                serialized_serie = SerieSerializer(serie).data
                serialized_season['series'].append(serialized_serie)

                serialized_seasons.append(serialized_season)
                serialized_seasons_dict[current_season_id] = serialized_season
            else:
                serialized_serie = SerieSerializer(serie).data
                serialized_seasons_dict[current_season_id]['series'].append(serialized_serie)

            previous_season_id = current_season_id
            i += 1

        return Response(serialized_seasons)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)

