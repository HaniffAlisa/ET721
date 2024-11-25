from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='path/to/default/image.jpg')

    def __str__(self):
        return self.title