from django.test import TestCase
from .models import *

# Create your tests here.
class ImageTestClass(TestCase):
    def setup(self):
        self.image_location = Location(location_name='Rift-Valley')
        self.image_loaction.save()

        self.image_category = Category(category_name='Food')
        self.image_category.save()

        self.image_food = Image(image_name='Kenya', image_description='Kenya kuna chakula', image_location='self.image_location', image_category=self.image_category)
        self.image_food.save_image()

    def test_instance(self):
        self.assertTrue(instance(self.image_food, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image_food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.image_food.save_image()
        self.image_food.delete_image()
        images = Image.objects.all()
        self.assertTrue((len(images)==0))   

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Rift-Valley')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(instance(self.location,Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location_name = 'Rift-Valley'
        self.location.update_location(self.location.id, new_location_name)
        updated_location = Location.objects.filter(location_name='Kenya')
        self.assertTrue(len(updated_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


