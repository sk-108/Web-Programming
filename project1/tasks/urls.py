from  django.urls import path

from . import views 

# to avoid namecollision between different apps we give app name 
app_name ="tasks"
urlpatterns = [
    path("",views.index,name = "index"),
    path("add",views.add,name = "add")

    ]