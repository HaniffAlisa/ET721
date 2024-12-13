from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=100)

class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class FeedbackPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title