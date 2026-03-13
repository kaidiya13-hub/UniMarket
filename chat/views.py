from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from items.models import Item
from .models import Message


@login_required(login_url='/admin/login/')
def marketplace(request):
    query = request.GET.get('q')
    items = Item.objects.filter(status='Active')

    if query:
        items = items.filter(title__icontains=query)

    items = items.order_by('-created_at')

    return render(request, 'marketplace.html', {
        'items': items,
        'query': query,
    })


@login_required(login_url='/admin/login/')
def chat_room(request, item_id, seller_id):
    item = get_object_or_404(Item, id=item_id)
    seller = get_object_or_404(User, id=seller_id)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Message.objects.create(
                sender=request.user,
                receiver=seller,
                item=item,
                content=content
            )

    messages = Message.objects.filter(item=item).order_by('timestamp')

    return render(request, 'chat_room.html', {
        'item': item,
        'seller_id': seller_id,
        'messages': messages,
    })


@login_required(login_url='/admin/login/')
def send_message(request, item_id, seller_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        seller = get_object_or_404(User, id=seller_id)
        content = request.POST.get('content')

        if content:
            message = Message.objects.create(
                sender=request.user,
                receiver=seller,
                item=item,
                content=content
            )

            return JsonResponse({
                'success': True,
                'sender': message.sender.username,
                'content': message.content,
                'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            })

        return JsonResponse({
            'success': False,
            'error': 'Message cannot be empty.'
        })

    return JsonResponse({
        'success': False,
        'error': 'Invalid request method.'
    })


@login_required(login_url='/admin/login/')
def get_messages(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    messages = Message.objects.filter(item=item).order_by('timestamp')

    data = []
    for message in messages:
        data.append({
            'sender': message.sender.username,
            'content': message.content,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })

    return JsonResponse({
        'messages': data
    })