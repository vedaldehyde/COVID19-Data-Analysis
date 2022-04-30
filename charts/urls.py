from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('continent_death/',views.deaths_per_continent),
    path('country_infection/',views.CountryInfection),
    path('average_infection/',views.AvgPopInf),
    path('dashboard/',views.dashboard),
]