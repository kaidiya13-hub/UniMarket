from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_item, name='post_item'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    
    # Add the hidden route for the AJAX request
    path('mark-sold/<int:item_id>/', views.mark_as_sold, name='mark_as_sold'),
]