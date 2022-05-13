from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import MySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from collections import Counter

# Create your views here.
def home(request):
    return render(request,'home.html')

# API view retreiving data representing all,“subway” routes of type 0 & type 1.
# Program list “long names” on the console.

@api_view()
def routes(request):
    api_link = "https://api-v3.mbta.com/routes?filter[type]=0,1"
    response_data = requests.get(api_link).json()
    api_dict = response_data['data']
    data = [{'long_name':res['attributes']['long_name']} for res in api_dict]
    return Response(data=data)

# Function to find maximum numbers of subway routes with from single direction_name
def max_stops(data):
    count_dict = {}
    count = 1
    for val in data:
        lst = list(val.values())[1]
        dict_key = str(lst)
        if dict_key in count_dict:
            count_dict[dict_key] = count_dict[dict_key] + 1
        else:
            count_dict[dict_key] = count
    max_count = max(count_dict, key= lambda x: count_dict[x])
    return max_count

# Function to find minimum numbers of subway routes from single direction_name
def min_stops(data):
    count_dict = {}
    count = 1
    for val in data:
        lst = list(val.values())[1]
        dict_key = str(lst)
        if dict_key in count_dict:
            count_dict[dict_key] = count_dict[dict_key] + 1
        else:
            count_dict[dict_key] = count
    min_count = min(count_dict, key= lambda x: count_dict[x])
    return min_count

# Function to finds subway routes from single direction_name with two or more stops
def count_2_more(data):
    count_dict = {}
    count = 1
    for val in data:
        lst = list(val.values())[1]
        dict_key = str(lst)
        if dict_key in count_dict:
            count_dict[dict_key] = count_dict[dict_key] + 1
        else:
            count_dict[dict_key] = count
    # count2 = min(count_dict, key= lambda x: count_dict[x])
    filtered_dict = {k:v for (k,v) in count_dict.items() if v>=2 }
    return list(filtered_dict)


# Program list subway routes with the most stops.
@api_view()
def most_stops(request):
    api_link = "https://api-v3.mbta.com/routes?filter[type]=0,1"
    response_data = requests.get(api_link).json()
    api_dict = response_data['data']
    data = [{'long_name':res['attributes']['long_name'],'direction_names': res['attributes']['direction_names'] } for res in api_dict]
    maxx = max_stops(data)
    filter_data = list(filter(lambda data: str(data['direction_names']) == maxx, data))
    return Response(data=filter_data)

# Program list subway routes with the fewest stops.
@api_view()
def fewest_stops(request):
    api_link = "https://api-v3.mbta.com/routes?filter[type]=0,1"
    response_data = requests.get(api_link).json()
    api_dict = response_data['data']
    data = [{'long_name':res['attributes']['long_name'],'direction_names': res['attributes']['direction_names'] } for res in api_dict]
    minn = min_stops(data)
    filter_data = list(filter(lambda data: str(data['direction_names']) == minn, data))
    return Response(data=filter_data)

# Program list subway routes with the two or more stops.
@api_view()
def two_more_routes(request):
    api_link = "https://api-v3.mbta.com/routes?filter[type]=0,1"
    response_data = requests.get(api_link).json()
    api_dict = response_data['data']
    data = [{'long_name':res['attributes']['long_name'],'direction_names': res['attributes']['direction_names'] } for res in api_dict]
    two_more = count_2_more(data)
    filter_data = list(filter(lambda data: str(data['direction_names']) in two_more, data))
    return Response(data=filter_data)

    