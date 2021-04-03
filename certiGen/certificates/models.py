from django.db import models

# Create your models here.

class Profile(models.Model):
    email = models.EmailField(max_length=254, blank=True, primary_key=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class certifs(models.Model):
    email = models.EmailField(max_length=254, blank=True)
    certificate_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.certificate_name

