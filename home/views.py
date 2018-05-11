from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'Misago', 'url': 'http://pypi.python.org/pypi/Misago/0.14.0'},
	{'name':'django-app-metrics', 'url': 'http://pypi.python.org/pypi/django-app-metrics/0.9.0'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
