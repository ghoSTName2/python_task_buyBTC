from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, "course/home.html",)
# Create your views here.
def buybtc(request):
    course = float(request.GET.get('course'))
    usdt = float(request.GET.get('usdt'))
    sum = usdt / course
    return render(request, 'course/coursebtc.html', {'buybtc':sum, 'cour':course, 'price':usdt })