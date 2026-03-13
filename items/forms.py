from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price', 'category', 'condition', 'description', 'image']
        
        # Apply Bootstrap CSS classes to form widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What are you selling?'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '£ 0.00'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }