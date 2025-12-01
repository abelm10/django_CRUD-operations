from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    qualified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.age} years old) - Qualified: {self.qualified}"