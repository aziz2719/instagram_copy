from django.shortcuts import render
from django.db.models import F, Count

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Comments, Likes
from .serializers import CommentSerializer, LikeSerializer, PublicationsSerializer, Publications
from .permissions import IsPublicationOwnerOrReadOnly, IsCommentOwnerOrReadOnly
from user.models import User

class PostLikesView(APIView):

    def get(self, request, pk):
        publication = Publications.objects.get(id=pk)
        likes = Likes.objects.values_list('user__username', flat=True).filter(publication=publication)
        return Response(likes)

class LikesView(APIView):

    def get(self, request, pk):
        user = request.user
        publication = Publications.objects.get(id=pk)
        if Likes.objects.filter(user=user, publication=publication).exists():
            Likes.objects.filter(user=user, publication=publication).delete()
            return Response('Like Deleted', status=status.HTTP_201_CREATED)
        else:
            Likes.objects.create(user=user, publication=publication)
            return Response('Like Created', status=status.HTTP_200_OK)
        
class PublicationsView(ModelViewSet):
    serializer_class = PublicationsSerializer
    queryset = Publications.objects.prefetch_related('post_images', 'post_comments').annotate(
        owner_nick_name=F('owner__username'),
        owner_avatar=F('owner__avatar'),
        likes_count=Count('post_likes')
    ).order_by('-date')
    lookup_field = 'pk'
    permission_classes = (IsPublicationOwnerOrReadOnly,)

    def get_object(self):
        obj = Publications.objects.prefetch_related('post_images').annotate(
            owner_nick_name=F('owner__username'),
            owner_avatar=F('owner__avatar'),
            likes_count=Count('post_likes')
        ).get(id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsCommentOwnerOrReadOnly, )