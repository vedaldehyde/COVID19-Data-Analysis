from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def g_numbers(request):
    return render(request,'charts/gnumbers.html')

def deaths_per_continent(request):
    return render(request,'charts/DeathsPerContinent.html')

def CountryInfection(request):
    return render(request,'charts/CountryInfection.html')

def AvgPopInf(request):
    return render(request,'charts/AvgPopInfected.html')

def dashboard(request):
    return render(request,'charts/dashboard.html')