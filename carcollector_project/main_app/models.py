from django.db import models
from django.urls import reverse
from django.utils import timezone

CAR_EXPENSES = (
    ('G', 'Gasoline'),
    ('M', 'Maintenance'),
    ('I', 'Insurance'),
    ('T', 'Tolls'),
    ('P', 'Parking'),
    ('W', 'Car Wash'),
    ('R', 'Registration'),
    ('D', 'Depreciation'),
    ('O', 'Oil Changes'),
    ('E', 'Emissions Testing'),
    ('C', 'Car Loan Payments'),
    ('S', 'Tire Replacement'),
    ('A', 'Accessories'),
    ('V', 'Vehicle Inspection'),
    ('H', 'Highway Fees'),
    ('L', 'Lease Payments'),
    ('N', 'New Car Purchase'),
    ('F', 'Fines and Tickets'),
    ('X', 'Miscellaneous Expenses'),
)

# Create your models here.

# Driver Model
class Driver(models.Model):
  name = models.CharField(max_length=50)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('driver_detail', kwargs={'pk': self.id})

# Car Model
class Car(models.Model):
  make = models.CharField(max_length=25)
  model = models.CharField(max_length=25)
  year = models.IntegerField(default=timezone.now().year)
  color = models.CharField(max_length=25)
  nickname = models.CharField(max_length=25, default='') 
  drivers = models.ManyToManyField(Driver)

  def __str__(self):
    return f"{self.nickname}: {self.make} {self.model}"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})
  

# History Model
class History(models.Model):
  date = models.DateField('Date')
  category = models.CharField(
    max_length=1,
    choices = CAR_EXPENSES,
    default=CAR_EXPENSES[0][0]  
  )
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.CharField(max_length=100, default='N/A')

  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    car_info = f"{self.car.make} {self.car.model} \"{self.car.nickname}\""
    return f"{car_info}: {self.get_category_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']