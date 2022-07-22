from django.db import models

class Cuisine(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.category

class Food(models.Model):
    category = models.ForeignKey(Cuisine, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    secondary_description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='food_images/')


    def __str__(self):
        return self.name