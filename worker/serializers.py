from rest_framework import serializers
from .models import Serie, SerieStatus, Season, SeasonStatus,Volume, VolumeStatus, Chapter, ChapterStatus

class SeasonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, season):
        request = self.context.get('request')
        return season.image_url(request) if request else None

    class Meta:
        model = Season
        fields = '__all__'

class SeasonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonStatus
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):
    season_id = serializers.IntegerField(source='season.id')  # Используем поле season_id для хранения идентификатора сезона
    image = serializers.SerializerMethodField()

    def get_image(self, serie):
        request = self.context.get('request')
        return serie.image_url(request) if request else None

    class Meta:
        model = Serie
        exclude = ('season',)  # Исключаем поле season из сериализации

class SerieStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieStatus
        fields = '__all__'

class VolumeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, volume):
        request = self.context.get('request')
        return volume.image_url(request) if request else None
    
    class Meta:
        model = Volume
        fields = '__all__'

class VolumeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeStatus
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    volume = VolumeSerializer()
    image = serializers.SerializerMethodField()

    def get_image(self, chapter):
        request = self.context.get('request')
        return chapter.image_url(request) if request else None

    class Meta:
        model = Chapter
        fields = '__all__'

class ChapterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterStatus
        fields = '__all__'