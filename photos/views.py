from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def gallery(request):
    date = dt.date.today()
    return render(request, 'all-picsPages/gallery.html', {"date": date,})