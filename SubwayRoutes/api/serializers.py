from dataclasses import field
import re
from rest_framework import serializers



class MySerializer(serializers.Serializer):
    id = serializers.CharField()
    long_name = serializers.CharField()
    type = serializers.CharField()
    direction_names = serializers.CharField()
    
