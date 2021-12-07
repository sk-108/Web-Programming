from django.urls import path

from . import views 

urlpatterns = [
    path("",views.index,name = "index"),
    path("sourav",views.sourav,name="sourav"),
    path("alok",views.alok,name="alok"),
    path("nitesh",views.nitesh,name="nitesh"),
    path("<str:name>",views.greet,name="greet")
]