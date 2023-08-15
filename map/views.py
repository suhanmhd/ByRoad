from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import traffic,road,Usermapping

from .models import Usermapping
import folium
from . import getroute

from geopy.geocoders import Nominatim



# Create your views here.


def showroute(request):
    
    return render(request,'map.html',)

def index(request):
    
    return render(request,'index.html',)






       
def showmap(request):
    return render(request,'map.html')

def home(request):
    if request.method=='POST':
        start=request.POST['startpoint']
        end=request.POST['destination']
        
        geolocator = Nominatim(user_agent="app11")
        location1 = geolocator.geocode(start)
        location2 = geolocator.geocode(end)
        lat1=location1.latitude
        long1=location1.longitude
        
        lat2=location2.latitude
        long2=location2.longitude


        figure = folium.Figure()
        lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)
        route=getroute.get_route(long1,lat1,long2,lat2)
        m = folium.Map(location=[(route['start_point'][0]),
                                 (route['start_point'][1])], 
                       zoom_start=10)
        m.add_to(figure)
        folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
        folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
        folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
        figure.render()
        context={'map':figure}
        return render(request,'home.html',context) 
    return render(request,'home.html')       

def userhome(request):
    return render(request,'userhome.html')    

def trafficissue(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            # if Usermapping.objects.filter(user=request.user,is_pwd=False,is_traffic=False):
               
                tname=request.POST['name']
                tphone=request.POST['phone']
                tplace=request.POST['place']
                tissue=request.POST['trafficissue']
                timage=request.FILES['image']
                traffic(tname=tname,user=request.user,tphone=tphone, tplace= tplace, tissue= tissue,timage=timage).save()
                messages.success(request,'complaint registered successfully') 
                return redirect(userhome)
            # else:
            #   messages.warning('incorrect username or password')
       
        else:
           messages.warning('Please login')
       
    
    return render(request,'trafficissue.html',)    

def roadissue(request):
     if request.method=='POST':
        if request.user.is_authenticated:
            # if Usermapping.objects.filter(user=request.user,is_pwd=False,is_traffic=False):
               
                name=request.POST['name']
                phone=request.POST['phone']
                place=request.POST['place']
                issue=request.POST['roadissue']
                image=request.FILES['image']
                road(name=name,user=request.user,phone=phone, place=place,issue=issue,image=image).save()
                messages.success(request,'complaint registered successfully') 
                return redirect(userhome)
        
        else:
           messages.warning('Please login')
       
    
     return render(request,'roadissue.html',)        


def trafficdept(request):
    trafficissues= traffic.objects.all()
    context={'trafficissues':trafficissues}
    
    return render(request,'traffic.html',context)       

def roads(request):
    roadissues =road.objects.all()
    context = {'roadissues':roadissues}
    
    return render(request,'road.html',context)           