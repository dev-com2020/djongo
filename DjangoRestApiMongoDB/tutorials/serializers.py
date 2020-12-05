from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Tutorials

class TutorialSerializer(serializers, ModelSerializer):

    class Meta:
        model = Tutorials
        fields = (
            'id',
            'title',
            'description',
            'published'
        )