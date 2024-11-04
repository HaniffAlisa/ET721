from django.db import models

"""class Todolist(models.Model):
    title = models.CharField(max_length=100, default="Untitled Task")  # Added default
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
"""

class Todolist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)  # Checkbox field for completion status

    def __str__(self):
        return self.title