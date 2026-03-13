from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_item, name='post_item'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('mark-sold/<int:item_id>/', views.mark_as_sold, name='mark_as_sold'),

    # Add routes for Edit and Delete
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

    path('<int:item_id>/', views.item_detail, name='item_detail'),
]