from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    SerieSerializer,
    SeasonSerializer, 
    ChapterSerializer, 
    VolumeSerializer
)

from .models import (
    Serie, 
    SerieStatus, 
    Season, 
    SeasonStatus, 
    Chapter, 
    ChapterStatus, 
    Volume, 
    VolumeStatus)

# Series
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def series_view(request):
    if request.method == 'GET':
        series = Serie.objects.all().select_related('season')
        series = series.prefetch_related('images')

        serialized_series = {}
        for serie in series:
            serialized_serie = SerieSerializer(serie, context={'request': request}).data
            serialized_serie['number'] = serie.number
            serialized_serie['images'] = [image.image_url(request) for image in serie.images.all()]

            serialized_serie['season_id'] = serie.season.id
            serialized_series[str(serie.number)] = serialized_serie

        return Response(serialized_series)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def series_status_view(request):
    if request.method == 'GET':
        user = request.user
        series = Serie.objects.all().select_related('season')

        series_statuses = SerieStatus.objects.filter(user=user, serie__in=series).select_related('serie')

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

            # Серии и связанные с ними изображения
            serie_data['images'] = [image.image_url(request) for image in serie.images.all()]

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

        # Добавляем prefetch_related для связанных моделей SeasonImage
        seasons = seasons.prefetch_related('images')

        serialized_seasons = {}
        for season in seasons:
            serialized_season = SeasonSerializer(season, context={'request': request}).data
            serialized_season['number'] = season.number

            # Сезоны и связанные с ними изображения
            serialized_season['images'] = [image.image_url(request) for image in season.images.all()]

            serialized_seasons[str(season.number)] = serialized_season

        return Response(serialized_seasons)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def seasons_status_view(request):
    if request.method == 'GET':
        user = request.user
        seasons = Season.objects.all()

        seasons_statuses = SeasonStatus.objects.filter(user=user, season__in=seasons).select_related('season')

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

            # Сезоны и связанные с ними изображения
            season_data['images'] = [image.image_url(request) for image in season.images.all()]

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


# Chapter
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def chapters_view(request):
    if request.method == 'GET':
        chapters = Chapter.objects.all()

        # Добавляем prefetch_related для связанных моделей Volume и ChapterImage
        chapters = chapters.prefetch_related(
            'volume',
            'images'
        )

        serializer = ChapterSerializer(chapters, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def chapters_status_view(request):
    if request.method == 'GET':
        user = request.user
        chapters = Chapter.objects.all()

        chapters_statuses = ChapterStatus.objects.filter(user=user, chapter__in=chapters).select_related('chapter')

        response_data = {}

        for chapter in chapters:
            status = next((status for status in chapters_statuses if status.chapter == chapter), None)
            if status is None:
                # Если статус не найден, добавляем главу со статусом "не просмотрено"
                chapter_data = ChapterSerializer(chapter).data
                chapter_data['status'] = 'not-watched'
            else:
                # Если статус найден, добавляем серию и её статус
                chapter_data = ChapterSerializer(chapter).data
                chapter_data['status'] = status.status

            # Главы и связанные с ними изображения
            chapter_data['images'] = [image.image_url(request) for image in chapter.images.all()]

            response_data[chapter.number] = {'chapter': chapter_data}

        if response_data:
            return Response(response_data)
        else:
            response_data = {
                'detail': 'У вас нет просмотренных глав.',
                'detail_en': 'You have no watched chapters.'
            }
            return Response(response_data, status=204)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)
    

@api_view(['POST'])
def chapters_save_status_view(request):
    chapter_number = request.data.get('chapter_number')
    status = request.data.get('status')

    user = request.user

    try:
        chapter = Chapter.objects.get(number=chapter_number)
    except Chapter.DoesNotExist:
        return Response({'detail': 'Chapter not found.'}, status=404)

    try:
        chapter_status = ChapterStatus.objects.get(user=user, chapter=chapter)
        chapter_status.status = status
        chapter_status.save()
    except ChapterStatus.DoesNotExist:
        chapter_status = ChapterStatus.objects.create(user=user, chapter=chapter, status=status)

    return Response({'detail': 'Status saved successfully.'})


# Volumes
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def volumes_view(request):
    if request.method == 'GET':
        volumes = Volume.objects.all().prefetch_related('chapters')

        # Добавляем prefetch_related для связанных моделей VolumeImage
        volumes = volumes.prefetch_related('images')

        serializer = VolumeSerializer(volumes, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


@api_view(['GET'])
def volumes_status_view(request):
    if request.method == 'GET':
        user = request.user
        volumes = Volume.objects.all().prefetch_related('chapters')


        volumes_statuses = VolumeStatus.objects.filter(user=user, volume__in=volumes).select_related('volume')

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

            # Томы и связанные с ними главы и изображения
            volume_data['chapters'] = [ChapterSerializer(chapter).data for chapter in volume.chapters.all()]
            volume_data['images'] = [image.image_url(request) for image in volume.images.all()]

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
    

@api_view(['POST'])
def volumes_save_status_view(request):
    volume_number = request.data.get('volume_number')
    status = request.data.get('status')

    user = request.user

    try:
        volume = Volume.objects.get(number=volume_number)
    except Volume.DoesNotExist:
        return Response({'detail': 'Volume not found.'}, status=404)

    try:
        volume_status = VolumeStatus.objects.get(user=user, volume=volume)
        volume_status.status = status
        volume_status.save()
    except VolumeStatus.DoesNotExist:
        volume_status = VolumeStatus.objects.create(user=user, volume=volume, status=status)

    return Response({'detail': 'Status saved successfully.'})


# Series anime release view
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def series_anime_realease_view(request):
    if request.method == 'GET':
        series = Serie.objects.all().order_by('anime_release_view_number')

        # Добавляем prefetch_related для связанных моделей Season, Serie, и SeasonImage
        series = series.prefetch_related(
            'season__images',
            'season__series__season__images'
        )

        serialized_seasons = []
        serialized_seasons_dict = {}
        previous_season_id = None

        for serie in series:
            current_season_id = serie.season.id

            if current_season_id != previous_season_id:
                season = serie.season
                serialized_season = SeasonSerializer(season, context={'request': request}).data
                serialized_season['series'] = []

                serialized_serie = SerieSerializer(serie, context={'request': request}).data
                serialized_season['series'].append(serialized_serie)

                serialized_seasons.append(serialized_season)
                serialized_seasons_dict[current_season_id] = serialized_season
            else:
                serialized_serie = SerieSerializer(serie, context={'request': request}).data
                serialized_seasons_dict[current_season_id]['series'].append(serialized_serie)

            previous_season_id = current_season_id

        return Response(serialized_seasons)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


# Series Chronological view
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def series_chronological(request):
    if request.method == 'GET':
        series = Serie.objects.all().order_by('chronological_view_number')

        # Добавляем prefetch_related для связанных моделей Season, Serie, и SeasonImage
        series = series.prefetch_related(
            'season__images',
            'season__series__season__images'
        )

        serialized_seasons = []
        serialized_seasons_dict = {}
        previous_season_id = None

        for serie in series:
            current_season_id = serie.season.id

            if current_season_id != previous_season_id:
                season = serie.season
                serialized_season = SeasonSerializer(season, context={'request': request}).data
                serialized_season['series'] = []

                serialized_serie = SerieSerializer(serie, context={'request': request}).data
                serialized_season['series'].append(serialized_serie)

                serialized_seasons.append(serialized_season)
                serialized_seasons_dict[current_season_id] = serialized_season
            else:
                serialized_serie = SerieSerializer(serie, context={'request': request}).data
                serialized_seasons_dict[current_season_id]['series'].append(serialized_serie)

            previous_season_id = current_season_id

        return Response(serialized_seasons)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)


# Series ranobe release
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def series_ranobe_release(request):
    if request.method == 'GET':
        series = Serie.objects.all().order_by('ranobe_release_number')

        # Добавляем prefetch_related для связанных моделей Season, Serie, и SeasonImage
        series = series.prefetch_related(
            'season__images',
            'season__series__season__images'
        )

        serialized_seasons = []
        serialized_seasons_dict = {}
        previous_season_id = None

        for serie in series:
            current_season_id = serie.season.id

            if current_season_id != previous_season_id:
                season = serie.season
                serialized_season = SeasonSerializer(season, context={'request': request}).data
                serialized_season['series'] = []

                serialized_serie = SerieSerializer(serie, context={'request': request}).data
                serialized_season['series'].append(serialized_serie)

                serialized_seasons.append(serialized_season)
                serialized_seasons_dict[current_season_id] = serialized_season
            else:
                serialized_serie = SerieSerializer(serie, context={'request': request}).data
                serialized_seasons_dict[current_season_id]['series'].append(serialized_serie)

            previous_season_id = current_season_id

        return Response(serialized_seasons)
    else:
        return Response({'detail': 'Method not allowed.'}, status=405)
