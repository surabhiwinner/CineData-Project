
from rest_framework import serializers

from .models import Movies,Artist

class MoviesSerializer(serializers.ModelSerializer):

    cast = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(),many = True)

    class Meta:
        
        model = Movies

        fields = '__all__'

        read_only_fields = ['uuid', 'active_status']
