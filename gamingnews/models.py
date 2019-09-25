from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


class Games(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='games/')
    vote = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.name


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to="user/", blank=True)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'Contact'
