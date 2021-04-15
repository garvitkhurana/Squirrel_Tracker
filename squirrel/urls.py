from django.urls import path

from . import views

app_name = 'squirrel'

urlpatterns = [
        path('', views.homepage),
        path('map/',views.map),
        path('sightings/stats/',views.get_statistics),
        path('sightings/add/',views.add_sighting),
        path('sightings/',views.sighting),
        path('sightings/<str:SQUIRREL_ID>/',views.edit_sighting),
        ]
