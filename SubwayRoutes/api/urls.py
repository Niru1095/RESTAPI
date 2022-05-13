from django.urls import path
from .views import home, routes , most_stops, fewest_stops , two_more_routes

urlpatterns = [
    path('',home ),
    path('routes/',routes ),
    path('most_stops/',most_stops ),
    path('fewest_stops/',fewest_stops ),
    path('two_more_routes/',two_more_routes ),
]