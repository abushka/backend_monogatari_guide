from rest_framework import serializers
from .models import Serie, SerieStatus, Season, Volume, Chapter

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
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

class ChapterSerializer(serializers.ModelSerializer):
    volume = VolumeSerializer()

    class Meta:
        model = Chapter
        fields = '__all__'