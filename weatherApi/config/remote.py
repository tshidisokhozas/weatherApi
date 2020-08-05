def getUrl(mode, units):
    baseUrl = "http://api.openweathermap.org/data/2.5/"
    baseUrl += mode + "?units=" + units + "&appid=7f62408c3864768103be1619fce3a7c1&q="

    return baseUrl


def getOneCallUrl(lat, lon):
    oneCallUrl = "https://api.openweathermap.org/data/2.5/onecall?"
    oneCallUrl += "lat=" + lat + "&lon=" + lon + "&exclude=current,minutely,hourly&units=metric&appid=7f62408c3864768103be1619fce3a7c1&q"
    return oneCallUrl

