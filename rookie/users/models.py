from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified','Not-specified')
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.

    def __str__(self):
        return self.username

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    phone = models.CharField(max_length=100,null=True)
    profileimg = models.ImageField(null=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICE,null=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True) 

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def lists_count(self):
        return self.lists.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()
    
    @property
    def following_count(self):
        return self.following.all().count()

