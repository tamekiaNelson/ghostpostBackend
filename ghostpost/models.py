from django.db import models
from django.utils.timezone import now


class GhostPoster(models.Model):
    post = models.CharField(max_length=280)
    is_boast = models.BooleanField(default=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.post}"
