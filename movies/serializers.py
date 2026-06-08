from rest_framework import serializers
from .models import Movie,Genre

class MovieSerializer(serializers.ModelSerializer):
    genre_name = serializers.StringRelatedField(source='genre', read_only=True,many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']
class DetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True,many=True)
    class Meta:
        model = Movie
        fields = '__all__'