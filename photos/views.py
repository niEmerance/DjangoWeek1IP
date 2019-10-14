from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,ImageLocation,ImageCategory
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist

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
        photos=Image.searchImage(search_term)
        message = f"{search_term}"

        return render(request,'all-picsPages/search.html',{'message':message,'photos':photos})
    else:
        message='no search yet'
        return render(request,'all-picsPages/search.html',{'message':message})

def imgDesc(request,imageId):
    try:
        imageIds=Image.objects.get(id=imageId)
    except ObjectDoesNotExist:
        raise Http404
    return render (request,'imgDesc.html',{'imageIds':imageIds})
