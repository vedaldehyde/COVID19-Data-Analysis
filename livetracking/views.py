from django.shortcuts import render
import requests


def getData(request):
    data=True
    result=None
    countries=None
    globalSummary=None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            globalSummary = result.json()['Global']
            countries=result.json()['Countries']
            data=False
        except:
            data=True

    return render(request,'livetracking/livedata.html',{'globalSummary':globalSummary,'countries':countries})
