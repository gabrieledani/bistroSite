from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=30)
    link = models.IntegerField(choices=((1, "Aluno"),
    									(2, "Parente de Aluno"),
                                        (3, "Professor"),
                                        (4, "Coordenação"),
                                        (5, "Outro")),
                                default=1)
    link_school = models.TextField(default='',blank=True)
    total = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    number = models.IntegerField(default=0)
    can_change = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30,blank=True)
    alergies = models.TextField(max_length=100,default='',blank=True)
    obs = models.TextField(max_length=100,default='',blank=True)
    gluten = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    kids_menu = models.BooleanField(default=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
