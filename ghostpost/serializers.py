from rest_framework.serializers import HyperlinkedModelSerializer
from ghostpost.models import GhostPoster


class GhostPostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GhostPoster
        fields = [
                'post',
                'is_boast',
                'up_votes',
                'down_votes',
                'total_votes',
                'submission_time'
                ]
