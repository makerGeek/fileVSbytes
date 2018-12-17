from django.db import models

# Create your models here.

class DoubleFile(models.Model):
    file_image = models.FileField()
    bytes_file = models.BinaryField()