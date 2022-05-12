from django.urls import path
from .views import home, routes , most_stops, fewest_stops

urlpatterns = [
    path('',home ),
    path('routes/',routes ),
    path('most_stops/',most_stops ),
    path('fewest_stops/',fewest_stops ),
]