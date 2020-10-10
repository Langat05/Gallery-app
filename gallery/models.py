from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',default='')
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    image_location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    image_category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)

    def __str__(self):
        self.save()


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=80, null= True)

    def __str__(self):
        return self.category