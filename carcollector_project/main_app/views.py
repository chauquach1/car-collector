from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import HistoryForm

# Add UpdateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'cars/home.html')

# Define the about view
def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'cars/about.html')

def cars_index(request):
  # We pass data to a template very much like we did in Express!
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  history_form = HistoryForm()
  return render(request, 'cars/detail.html', {
    'car': car ,
    'history_form': history_form
  })

def add_history(request, pk):
  # create a ModelForm instance using the data in request.POST
  form = HistoryForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_history = form.save(commit=False)
    new_history.car_id = pk
    new_history.save()
  return redirect('car_detail', car_id=pk)

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  # Special string pattern Django will use
  def get_success_url(self):
      # Use reverse to generate the URL based on the car_id of the newly created Car instance
      return reverse('car_detail', args=[self.object.id])
class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a car by excluding the name field!
  fields = '__all__'
  
class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'