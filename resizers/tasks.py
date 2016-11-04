from celery.decorators import task
from PIL import Image as PImage
from .models import Image
from io import BytesIO
from django.core.files.base import ContentFile
from datetime import datetime
import os


@task(name="resize_uploaded_image")
def resize_uploaded_image(idx):
    instance = Image.objects.get(id=idx)
    im = PImage.open(instance.original_image.file)
    im_format = im.format
    im = im.resize((im.width // 2, im.height // 2), PImage.LANCZOS)
    
    temp_handle = BytesIO()
    im.save(temp_handle, im_format)
    temp_handle.seek(0)
    
    instance.resized_image.save(
        os.path.split(instance.original_image.name)[-1],
        ContentFile(temp_handle.read()),
        save=False
    )
    instance.resized_at = datetime.now()
    instance.save()
