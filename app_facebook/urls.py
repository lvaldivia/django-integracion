from django.conf.urls import url
from app_facebook import views

urlpatterns = [
    url(r'^game/',views.Home.as_view(),name='home'),
    #url(r'^juego2/',views.MiOtraPagina.as_view(),
    #name='otrapagina' ),
    
]