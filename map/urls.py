from .import views
from map.controller import authview
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [ 
    path('home',views.home,name='home'),
    path('userhome',views.userhome,name='userhome'),
    path('trafficissue',views.trafficissue,name='trafficissue'),
    path('roadissue',views.roadissue,name='roadissue'),
    path('traffic',views.trafficdept,name='traffic'),
    path('roads',views.roads,name='road'),
    path('login',authview.user_login,name='login'),
    path('trafficlogin',authview.traffic_login,name='traffic_login'),
    path('pwdlogin',authview.pwd_login,name='pwd_login'),
     path('logout',authview.user_logout,name='logout'),
    path('signup',authview.signup,name='signup'),
    path('map',views.showroute,name='showroute'),
    path('showmap',views.showmap,name='showmap'),


    path('index',views.index,name='index'),


   

]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)