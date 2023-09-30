# artist/serializers.py

from rest_framework import serializers
from .models import Artist, Work
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'password']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link', 'work_type']

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'works']
