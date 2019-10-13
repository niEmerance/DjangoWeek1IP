from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def gallery(request):
    date = dt.date.today()
    photos = Image.save_Image()
    return render(request, 'all-picsPages/gallery.html', {"date": date,"photos":photos})
