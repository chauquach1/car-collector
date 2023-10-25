from django.urls import path
from . import views

urlpatterns = [
  # Cars URLs
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='index'),
  path('cars/<int:car_id>/', views.cars_detail, name='car_detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:pk>/add_history/', views.add_history, name='add_history'),
  path('cars/<int:pk>/assoc_driver/<int:driver_pk>/', views.assoc_driver, name='assoc_driver'),

  # Drivers URL
  path('drivers/', views.DriverList.as_view(), name='drivers_index'),
  path('drivers/<int:pk>/', views.DriverDetail.as_view(), name='drivers_detail'),
  path('drivers/create/', views.DriverCreate.as_view(), name='drivers_create'),
  path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name='drivers_update'),
  path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name='drivers_delete'),
]