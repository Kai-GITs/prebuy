import datetime
import json

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST

from main.forms import NewsForm
from main.models import News

# Create your views here.

@login_required
@require_POST
def add_news_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail") or None
    is_featured = request.POST.get("is_featured") in ["on", "true", "1"]

    if not all([name, price, description, category]):
        return HttpResponseBadRequest("Missing required fields")

    try:
        price = int(price)
    except ValueError:
        return HttpResponseBadRequest("Invalid price")

    valid_categories = dict(News.CATEGORY_CHOICES)
    if category not in valid_categories:
        return HttpResponseBadRequest("Invalid category")

    new_news = News(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=request.user,
    )
    new_news.save()

    return JsonResponse(
        {
            "id": str(new_news.id),
            "name": new_news.name,
            "price": new_news.price,
            "description": new_news.description,
            "category": new_news.category,
            "thumbnail": new_news.thumbnail,
            "is_featured": new_news.is_featured,
            "news_views": new_news.news_views,
            "created_at": new_news.created_at.isoformat(),
            "user_id": new_news.user_id,
            "user_username": new_news.user.username if new_news.user else None,
        },
        status=201,
    )


@login_required
@require_POST
def edit_news(request, id):
    news = get_object_or_404(News, pk=id, user=request.user)
    form = NewsForm(request.POST, instance=news)

    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)

    updated_news = form.save()

    return JsonResponse(
        {
            "id": str(updated_news.id),
            "name": updated_news.name,
            "price": updated_news.price,
            "description": updated_news.description,
            "category": updated_news.category,
            "thumbnail": updated_news.thumbnail,
            "is_featured": updated_news.is_featured,
            "news_views": updated_news.news_views,
            "created_at": updated_news.created_at.isoformat(),
            "user_id": updated_news.user_id,
            "user_username": updated_news.user.username if updated_news.user else None,
        }
    )


@login_required
@require_POST
def delete_news(request, id):
    news = get_object_or_404(News, pk=id, user=request.user)
    news.delete()
    return JsonResponse({"status": "deleted"})

@login_required
def logout_user(request):
    logout(request)
    if request.method == "POST":
        response = JsonResponse({"redirect": reverse('main:login')})
    else:
        response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode())
        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid payload"}, status=400)

        form = AuthenticationForm(request, data=payload)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors}, status=400)

        user = form.get_user()
        login(request, user)
        response = JsonResponse({"redirect": reverse("main:show_main")})
        response.set_cookie("last_login", str(datetime.datetime.now()))
        return response

    form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})

def register(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode())
        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid payload"}, status=400)

        form = UserCreationForm(payload)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors}, status=400)

        form.save()
        return JsonResponse({"redirect": reverse("main:login")}, status=201)

    form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def show_xml(request):
     news_list = News.objects.all()
     xml_data = serializers.serialize("xml", news_list)
     return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    news_list = News.objects.all()
    data = [
        {
            'id': str(news.id),
            'name': news.name,
            'price': news.price,
            'description': news.description,
            'category': news.category,
            'thumbnail': news.thumbnail,
            'news_views': news.news_views,
            'created_at': news.created_at.isoformat() if news.created_at else None,
            'is_featured': news.is_featured,
            'user_id': news.user.id if news.user else None,
            'user_username': news.user.username if news.user else None,
        }
        for news in news_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, news_id):
   try:
       news_item = News.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except News.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, news_id):
    try:
        news = News.objects.select_related('user').get(pk=news_id)
        data = {
            'id': str(news.id),
            'name': news.name,
            'price': news.price,
            'description': news.description,
            'category': news.category,
            'thumbnail': news.thumbnail,
            'news_views': news.news_views,
            'created_at': news.created_at.isoformat() if news.created_at else None,
            'is_featured': news.is_featured,
            'user_id': news.user.id if news.user else None,
            'user_username': news.user.username if news.user else None,
        }
        return JsonResponse(data)
    except News.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    context = {
        'app': 'PreBuy',
        'name': request.user.username,
        'class': 'PBP C',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

@login_required(login_url='/login')
def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)
