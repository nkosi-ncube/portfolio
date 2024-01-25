from django.db import models

# Create your models here.
class Blog(models.Model):
    topic  = models.CharField(max_length=100)
    content  = models.TextField(max_length=500)
    time_stamp = models.DateField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.topic
class Testimonies(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

class Contacts(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.email