from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from backend_app.models import GhostpostModel
from backend_app.serializers import GhostpostSerializer


class GhostpostViewset(viewsets.ModelViewSet):
    queryset = GhostpostModel.objects.all()
    serializer_class = GhostpostSerializer

    @action(detail=False)
    def Boast(self, request):
        boast = GhostpostModel.objects.filter(post_type='Boast').order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)


    @action(detail=False)
    def Roast(self, request):
        roast = GhostpostModel.objects.filter(post_type='Roast').order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['get', 'post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_vote += 1
        post.save()
        return Response({'status': 'upvoted'})


    @action(detail=True, methods=['get', 'post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_vote += 1
        post.save()
        return Response({'status': 'downvoted'})
    

