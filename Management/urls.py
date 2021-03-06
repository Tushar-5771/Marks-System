from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index,name="index"),
    path('Home',views.Home,name="Home"),
    path('addMarks',views.addMarks,name="Add"),
    path('viewMarks',views.viewMarks,name="view"),
    path('updateMarks',views.updateMarks,name="update"),
    path('getData',views.getMarks,name="getData"),
    path('logout',views.userLogOut,name="logout")
]