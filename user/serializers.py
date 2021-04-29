from rest_framework import serializers

from publications.models import Publications
from publications.serializers import PublicationImagesSerializer
from user.models import User, Favorite


class PublicationsForUserSerializer(serializers.ModelSerializer):
    post_images = PublicationImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Publications
        fields = ('id', 'text', 'date', 'post_images')


class UserSerializer(serializers.ModelSerializer):
    post_owner = PublicationsForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('phone', 'site', 'bio', 'avatar', 'username', 'first_name', 'last_name', 'email', 'post_owner')


