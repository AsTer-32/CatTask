from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cats')

    def __str__(self):
        return self.name
