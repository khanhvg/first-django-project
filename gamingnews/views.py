from django.shortcuts import render
from .models import Games, Article
from .forms import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    game_list = Games.objects.order_by('name')
    game_dict = {'games': game_list}
    return render(request, 'gamingnews/home.html', context=game_dict)


def game_detail(request, id=None):
    game = Games.objects.get(pk=id)
    return render(request, 'gamingnews/single-game-review.html', context={"game": game})


def game_review(request):
    game_list = Games.objects.order_by('name')
    game_dict = {'games': game_list}
    return render(request, 'gamingnews/game-review.html', context=game_dict)


def game_result(request):
    game_list = Games.objects.order_by('name')
    game_search = []
    count = 0
    if request.method == "GET":
        games = request.GET.get("games")
        for item in game_list:
            if games.lower() in item.name.lower():
                game_search.append(item)
        if len(game_search) > 0:
            count = len(game_search)
    return render(request, "gamingnews/game-result.html", context={"game_result": game_search, "count": count})


def article(request):
    art = Article.objects.order_by("name")
    games = Games.objects.order_by("name")
    part = int(len(games) / 2)
    lst1 = []
    for i in range(0, part, 1):
        lst1.append(games[i])
    ar = Article.objects.order_by("name")
    part2 = int(len(ar) / 2)
    lst2 = []
    for i in range(0, part2, 1):
        lst2.append(ar[i])
    return render(request, 'gamingnews/post.html', context={'article': art, "games": lst1, "art": lst2})


def article_detail(request, id=None):
    art = Article.objects.get(pk=id)
    gaming = Games.objects.order_by("name")
    part = int(len(gaming) / 2)
    lst1 = []
    for i in range(0, part, 1):
        lst1.append(gaming[i])
    artic = Article.objects.order_by("name")
    part2 = int(len(artic) / 2)
    lst2 = []
    for i in range(0, part2, 1):
        lst2.append(artic[i])
    return render(request, 'gamingnews/single-post.html', context={"article": art, "games": lst1, "art": lst2})


def contact(request):
    registered = False
    if request.method == "POST":
        form_contact = FormContact(data=request.POST)
        if form_contact.is_valid():
            registered = form_contact.save()
            registered.save()
            registered = True
    else:
        form_contact = FormContact()
    response = render(request, 'gamingnews/contact.html', {'contact_form': form_contact, 'registered': registered})
    response.delete_cookie('visit_time')
    return response
