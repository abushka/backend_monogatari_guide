from rest_framework import serializers
from .models import Serie, SerieStatus, Season

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
