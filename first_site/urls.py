from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='first-site'),
    path('circle/',views.circle,name="circle"),
    path('geometry/',views.geometry,name="geometry"),
    path('intersection/',views.intersection,name="intersection"),
    path('physics/',views.physics,name="physics"),
]
