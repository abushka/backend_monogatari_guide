from rest_framework import serializers
from .models import Serie, SerieStatus, Season, SeasonStatus,Volume, VolumeStatus, Chapter, ChapterStatus

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class SeasonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonStatus
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()

    class Meta:
        model = Serie
        fields = '__all__'

class SerieStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieStatus
        fields = '__all__'

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'

class VolumeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeStatus
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    volume = VolumeSerializer()

    class Meta:
        model = Chapter
        fields = '__all__'

class ChapterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterStatus
        fields = '__all__'