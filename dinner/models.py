from django.db import models


class Vote(models.Model):
    '''
    Model for a vote, just a name and place to eat
    '''
    name = models.CharField(max_length=50)
    dinner = models.CharField(max_length=255)
