from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

# Create your models here.
''' Defined function reference
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    game = models.CharField(max_length=100, default="Pong")
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    description = models.CharField(max_length=200, null=True)

    def __str__(self): return self.title

    def get_absolute_url(self): return reverse("sessionDetails", args=[str(self.id)])
