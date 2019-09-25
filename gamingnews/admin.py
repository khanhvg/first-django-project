from django.contrib import admin
from .models import Category, Games, UserProfileInfo, Contact, Article

# Register your models here.

admin.site.register(Category)
admin.site.register(Games)
admin.site.register(UserProfileInfo)
admin.site.register(Contact)
admin.site.register(Article)
