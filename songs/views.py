from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class SongView(ListCreateAPIView, RetrieveAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get (self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs['pk']) 
        serializer.save(album=album)
    
    def get_queryset(self):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return Song.objects.filter(album=album)