from django.urls import path,include
from .views import home, Menu, About, Con, Pro


app_name = "main"

urlpatterns = [
    path("", home, name="index"),
    path("menu/", Menu.as_view(), name="menu"),
    # path("gallery/", Pro.as_view(), name="gallery"),
    path("about/", About.as_view(), name="about"),
    path("con/", Con.as_view(), name="con"),
    path('dashboard/', include('clinet.urls'))

]