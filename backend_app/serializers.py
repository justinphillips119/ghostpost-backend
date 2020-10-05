from rest_framework import serializers
from django.db.models import fields
from backend_app.models import GhostpostModel


class GhostpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GhostpostModel
        fields = [
            'id',
            'post_type', 
            'content', 
            'upvote', 
            'downvote', 
            'post_date'
        ]