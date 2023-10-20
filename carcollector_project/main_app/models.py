from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Car(models.Model):
  make = models.CharField(max_length=25)
  model = models.CharField(max_length=25)
  year = models.IntegerField(default=timezone.now().year)
  color = models.CharField(max_length=25)
  nickname = models.CharField(max_length=25, default='') 

  def __str__(self):
    return f"{self.nickname}: {self.make} {self.model}"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})