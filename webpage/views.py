from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'webpage/index.html')


def news(request):
    temp = ["문재인", "아베", "트럼프"]
    context = {"president": temp}
    return render(request, 'webpage/news.html', context=context)


def contact(request):
    return render(request, 'webpage/contact.html')


def about(request):
    return render(request, 'webpage/about.html')

# def test(request, **kwargs):
#     temp = kwargs['year'] * 2
#     return HttpResponse(temp)

class test(View):
    def get(self, request, *args, **kwargs):
        temp = kwargs['year']
        response = HttpResponse(temp)
        return response
