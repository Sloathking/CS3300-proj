from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
''' Definied function reference
    #Define default String to return the name for representing the Model object.
    def __str__(self):
        return self.name
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
'''
class Player(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self): return self.username
    def get_absolute_url(self): return reverse("player-detail", args=[str(self.id)])

class Session(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    description = models.CharField(max_length=200, null=True)

    def __str__(self): return self.title

    def get_absolute_url(self): return reverse("session-detail", args=[str(self.id)])
    
