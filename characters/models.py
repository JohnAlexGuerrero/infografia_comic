from django.db import models
from django.urls import reverse

select_race = (
    ('Hu', 'humano'),
    ('Mu', 'mutante'),
    
)

select_gender = (
    ('M','male'),
    ('F','female'),
)


class Profession(models.Model):
    name = models.CharField(("nombre"), max_length=50, unique=True)
    description = models.CharField(("description"), max_length=200, null=True)

    class Meta:
        verbose_name = ("Profession")
        verbose_name_plural = ("Professions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Profession_detail", kwargs={"pk": self.pk})

class Weapon(models.Model):
    name = models.CharField(("name"), max_length=50, unique=True)
    description = models.CharField(("description"), max_length=100, null=True)
    image = models.ImageField(("image"), upload_to='weapons/')

    class Meta:
        verbose_name = ("Weapon")
        verbose_name_plural = ("Weapons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Weapon_detail", kwargs={"pk": self.pk})


class Abilities(models.Model):
    name = models.CharField(("nombre"), max_length=50, unique=True)
    description = models.CharField(("description"), max_length=200, null=True)

    class Meta:
        verbose_name = ("Abilities")
        verbose_name_plural = ("Abilities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Abilities_detail", kwargs={"pk": self.pk})


class Character(models.Model):
    alias = models.CharField(("alias"), max_length=50, unique=True)
    name = models.CharField(("nombre"), max_length=100, unique=True)
    race = models.CharField(("raza"), max_length=8, choices=select_race, default=select_gender[0])
    gender = models.CharField(("genero"), max_length=8, choices=select_gender)
    length = models.FloatField(("estatura"), null=True)
    weight = models.FloatField(("peso"), null=True)
    popularity = models.IntegerField(("popularidad"), default=1)
    is_died = models.BooleanField(("vivo"), default=True)
    avatar = models.ImageField(("avatar"), upload_to='characters/', null=True)
    logo = models.ImageField(("logo"), upload_to='logos/')
    created_at_year = models.IntegerField(("año de creacion"), null=True)
    occupation = models.ManyToManyField(Profession, verbose_name=("occupations"))
    bio = models.TextField(("biografia"), null=True)
    weapons = models.ManyToManyField(Weapon, verbose_name=("weapons"))
    abilities = models.ManyToManyField(Abilities, verbose_name=("abilities"))
    
    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")

    def __str__(self):
        return self.alias

    def get_absolute_url(self):
        return reverse("Character_detail", kwargs={"pk": self.pk})

