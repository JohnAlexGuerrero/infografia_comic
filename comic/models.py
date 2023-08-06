from django.db import models
from django.urls import reverse

class Book(models.Model):
    image = models.ImageField(("imagen"), upload_to='thumbnails/', default='/static/media/thumbnails/no-img.jpg')
    title = models.CharField(("nombre"), max_length=100, unique=True)
    created_at = models.DateField(("creacion"), auto_now_add=True)
    updated_at = models.DateField(("actualizacion"), auto_now_add=True)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
