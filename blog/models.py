from django.db import models

class ImageInput(models.Model):
    face_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name