from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image
from .tasks import resize_uploaded_image


@receiver(post_save, sender=Image)
def resize_image(sender, instance, created, **kwargs):
    if created:
        resize_uploaded_image.delay(instance.id)
