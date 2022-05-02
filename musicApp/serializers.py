''' Copyright (c) 2019 Construction Casualty Insurance, Inc.

    REST serializer classes
'''

from pprint import pprint

from django.utils.crypto import get_random_string

from rest_framework import serializers
from .models import Works

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'title', 'iswc', 'contributors']
