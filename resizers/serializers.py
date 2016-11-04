from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'original_image', 'resized_image', 'created_at', 'resized_at', 'url')
        read_only_fields = ('resized_image', 'created_at', 'resized_at')
