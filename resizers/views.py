from .serializers import ImageSerializer
from .models import Image
from rest_framework import viewsets
from django.shortcuts import render


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def statistics(request):
    return render(
        request,
        "index.html",
        {
            "images": Image.objects.order_by("id")
        }
    )
