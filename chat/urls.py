from django.urls import path
from . import views

urlpatterns = [
    path('marketplace/', views.marketplace, name='marketplace'),
    path('chat/<int:item_id>/<int:seller_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:item_id>/<int:seller_id>/send/', views.send_message, name='send_message'),
    path('chat/<int:item_id>/messages/', views.get_messages, name='get_messages'),
]