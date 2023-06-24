from django.db import models

from users.serializers import UserSerializer


class Album(models.Model):    
    class Meta:
        ordering = ["id",] #ou ['id'], estava com [] antes

    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="albums",
    )
