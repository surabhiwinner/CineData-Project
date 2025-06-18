
from rest_framework import serializers

from .models import Movies,Artist

class MoviesListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Movies

        fields = '__all__'

        read_only_fields = ['uuid', 'active_status']

        depth = 1

class MoviesCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Movies

        exclude = ['cast','active_status','uuid']

