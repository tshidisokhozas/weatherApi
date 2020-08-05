import requests
from django.shortcuts import render

from .config.remote import getUrl, getOneCallUrl
from .config.timestamp import get_Date,get_time,_time
from .forms import Post


def index(request):
    def post():
        city = ""

        if request.method == "POST":
            form = Post(request.POST)

            if form.is_valid():
                city = form.cleaned_data.get('city')

        get_weather = getUrl("weather", "metric") + city

        return get_weather

    response = requests.get(post())

    if response.status_code == 200:

        data = response.json()

        timestamp = data["dt"]
        date = get_Date(timestamp)
        time = get_time(timestamp)
        name = data["name"]
        time = time
        date = date
        temp = data["main"]["temp"]
        country = data["sys"]["country"]
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        data_context = {

            "name": name,
            "time": time,
            "date": date,
            "temp": int(temp),
            "country": country,
            "description": description,
            "icon": icon,

        }


    else:

        data_context = {}

    data_context["form"] = Post()
    return render(request, 'views/index.html', data_context)
