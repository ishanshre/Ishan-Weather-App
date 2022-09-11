from django.shortcuts import render
from django.views import View
import json
import urllib.request
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'weather/index.html')
    
    def post(self, request):
        city = request.POST.get('city')
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=2934e27de853b10e244bcb630d0e5de6').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'])+'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']), 
        }
        context = {
            'city':city,
            'data':data,
        }
        return render(request, 'weather/index.html', context)
