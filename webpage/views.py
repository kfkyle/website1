from django.shortcuts import render
from .models import Home
from .models import Service

from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        title_page =  Home.objects.get(name='Title Page')
        services_header =  Home.objects.get(name='Services Header')
        services =  Service.objects.filter(name='Services')
        why_us =  Home.objects.get(name='Why Us')
        careers =  Home.objects.get(name='Careers')
        about_us =  Home.objects.get(name='About Us')

        context = {
        'home': title_page,
        'services_header': services_header,
        'services': services,
        'why_us': why_us,
        'careers': careers,
        'about_us': about_us
        }

        return render(request, 'webpage/home_view.html', context)
