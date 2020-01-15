from ghostpost import models, serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class GhostPostView(viewsets.ModelViewSet):
    queryset = models.GhostPoster.objects.all()
    serializer_class = serializers.GhostPostSerializer

    @action(detail=True, methods=['get'])
    def up_votes(self, request, pk=None):
        post = models.GhostPoster.objects.get(pk=pk)
        post.total_votes += 1
        post.save()
        return Response({'status': 'like'})

    def down_votes(self, request, pk=None):
        post = models.GhostPoster.objects.get(pk=pk)
        post.down_votes += 1
        post.total_votes -= 1
        post.save()
        return Response({'status': 'unlike'})
