from django.db import models

# Create your models here.

class Transfer(models.Model):
    names = models.CharField(max_length = 300)
    age = models.IntegerField(default=0)
    playerImage = models.CharField(max_length = 300)
    playerLink = models.CharField(max_length = 800)
    fromTeam = models.CharField(max_length = 100)
    fromTeamImage = models.CharField(max_length = 800)
    toTeam = models.CharField(max_length = 100)
    toTeamImage = models.CharField(max_length = 800)
    position = models.CharField(max_length = 100)
    fee = models.CharField(max_length = 100)
    date = models.CharField(max_length = 100)

    def __str__(self):
        return self.names