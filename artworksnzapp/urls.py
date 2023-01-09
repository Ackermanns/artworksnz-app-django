from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('artists/', views.artists),
    path('artists/<artistkey>/', views.artistshow),
    path('artworks/', views.artworks),
    path('artworks/<artworkkey>/', views.artworkshow),
    path('addartwork/<int:artistkey>/', views.addartwork),
    path('addartist/', views.addartist),
    path('delete_artist/<artistkey>/', views.delete_artist),
    path('delete_artwork/<artworkkey>/', views.delete_artwork),
    path('edit_artwork/<artworkkey>/', views.edit_artwork),
    path('edit_artist/<artistkey>/', views.edit_artist),
]
