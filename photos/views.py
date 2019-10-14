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

def searchImage(request):
    if 'image' in request.GET and request.GET['image']:
        search_term=request.GET.get('image')
        images=Image.searchImage(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{'message':message,'images':images})
    else:
        message='no search yet'
        return render(request,'search.html',{'message':message})
