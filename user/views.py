from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user.models import User, Favorite
from user.permissions import IsUserOwnerOrReadOnly
from user.serializers import UserSerializer
from rest_framework.views import APIView
from publications.models import Publications
from rest_framework.response import Response
from rest_framework import status


class UserView(ModelViewSet):
    queryset = User.objects.prefetch_related('post_owner')
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )

class UserFavoriteView(APIView):

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        favorite = Favorite.objects.values_list('publication__text', flat=True).filter(user=user)
        return Response(favorite)

class FavoriteView(APIView):

    def get(self, request, pk):
        user = request.user
        publication = Publications.objects.get(id=pk)
        favorite = Favorite.objects.values_list('user__username', flat=True).filter(publication=publication)
        if Favorite.objects.filter(user=user, publication=publication).exists():
            Favorite.objects.filter(user=user, publication=publication).delete()
            return Response('Favorite Deleted', status=status.HTTP_201_CREATED)
        else:
            Favorite.objects.create(user=user, publication=publication)
            return Response('Favorite Created', status=status.HTTP_200_OK)