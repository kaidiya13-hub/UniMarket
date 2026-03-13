from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Item
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Require user authentication to post an item (Requirement M3)
@login_required(login_url='/admin/login/')
def post_item(request):
    if request.method == 'POST':
        # Handle form submission including image files
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Create item instance without saving to database yet
            new_item = form.save(commit=False)
            # Assign the currently logged-in user as the seller
            new_item.seller = request.user
            # Save the item to the database
            new_item.save()
            # Redirect to admin dashboard after successful submission
            return redirect('/admin/items/item/')
    else:
        # Render an empty form for GET requests
        form = ItemForm()

    return render(request, 'items/post_item.html', {'form': form})
# Dashboard view (Requirement S1, S2)
@login_required(login_url='/admin/login/')
def seller_dashboard(request):
    # Retrieve only the items posted by the currently logged-in user
    # Order them by creation time (newest first)
    my_items = Item.objects.filter(seller=request.user).order_by('-created_at')
    
    # Pass the retrieved items to the template
    return render(request, 'items/seller_dashboard.html', {'items': my_items})
# AJAX endpoint to mark an item as sold (Client-side Interaction requirement)
@login_required(login_url='/admin/login/')
def mark_as_sold(request, item_id):
    if request.method == 'POST':
        # Safely get the item, ensuring the logged-in user is the actual seller
        item = get_object_or_404(Item, id=item_id, seller=request.user)
        
        # Update status and save to database
        item.status = 'Sold'
        item.save()
        
        # Return a JSON response back to the JavaScript frontend
        return JsonResponse({'success': True, 'new_status': 'Sold'})
    
    # Return error if not a POST request
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)
# Edit an existing item (Requirement S1/S2 context)
@login_required(login_url='/admin/login/')
def edit_item(request, item_id):
    # Ensure the user can only edit their own items
    item = get_object_or_404(Item, id=item_id, seller=request.user)
    
    if request.method == 'POST':
        # Pass the existing item instance to the form to update it
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        # Pre-fill the form with existing item data
        form = ItemForm(instance=item)
        
    return render(request, 'items/edit_item.html', {'form': form, 'item': item})

# Delete an item safely
@login_required(login_url='/admin/login/')
def delete_item(request, item_id):
    # Ensure the user can only delete their own items
    item = get_object_or_404(Item, id=item_id, seller=request.user)
    
    if request.method == 'POST':
        item.delete()
        return redirect('seller_dashboard')
        
    return render(request, 'items/delete_confirm.html', {'item': item})
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'items/item_detail.html', {'item': item})