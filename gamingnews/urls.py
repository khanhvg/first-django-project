from . import views
from django.urls import path

app_name = 'gamingnews'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('game_review/', views.game_review, name="game_review"),
    path('game_detail/<int:id>', views.game_detail, name='game_detail'),
    path('game_search', views.game_result, name='game_result'),
    path('article/', views.article, name="article"),
    path('article_detail/<int:id>', views.article_detail, name="article_detail"),
]
