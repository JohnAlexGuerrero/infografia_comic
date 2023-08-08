from django.db import models
from django.urls import reverse

from characters.models import Character

class Book(models.Model):
    thumbnail = models.ImageField(("imagen"), upload_to='thumbnails/')
    title = models.CharField(("nombre"), max_length=100, unique=True)
    characters = models.ManyToManyField(Character, verbose_name=("characters"))
    # created_at = models.DateField(("creacion"), auto_now_add=True)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})


