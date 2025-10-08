from django.urls import path

from main.views import (
    add_news_entry_ajax,
    delete_news,
    edit_news,
    login_user,
    logout_user,
    register,
    show_json,
    show_json_by_id,
    show_main,
    show_news,
    show_xml,
    show_xml_by_id,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('news/<uuid:id>/', show_news, name='show_news'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/news/create/', add_news_entry_ajax, name='add_news_entry_ajax'),
    path('api/news/<uuid:id>/update/', edit_news, name='edit_news'),
    path('api/news/<uuid:id>/delete/', delete_news, name='delete_news'),
]
