from django.db import models
from channels.binding.websockets import WebsocketBinding

class Image(models.Model):
    original_image = models.ImageField(upload_to="original_images/")
    resized_image = models.ImageField(upload_to="resized_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    resized_at = models.DateTimeField(null=True)

    def __str__(self):
        return "Image id: {}".format(self.id)

class ImageBinding(WebsocketBinding):
    model = Image
    stream = "image"
    fields = ["original_image", "resized_image", "created_at", "resized_at"]

    @classmethod
    def group_names(cls, *args, **kwargs):
        return ["binding.values"]

    def has_permission(self, user, action, pk):
        return True
