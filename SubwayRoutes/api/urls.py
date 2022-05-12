from django.urls import path
from .views import home, my_view, most_stops, fewest_stops

urlpatterns = [
    path('',home ),
    path('routes/',my_view ),
    path('most_stops/',most_stops ),
    path('fewest_stops/',fewest_stops ),
]