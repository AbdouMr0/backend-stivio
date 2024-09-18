from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'available_sizes', 'image_url']

    def clean_available_sizes(self):
        sizes = self.cleaned_data['available_sizes'].split(',')
        category = self.cleaned_data['category']
        valid_sizes = [choice[0] for choice in Product.SIZE_CHOICES.get(category, [])]
        if not all(size in valid_sizes for size in sizes):
            raise forms.ValidationError(f"Some sizes are not valid for category '{category}'")
        return self.cleaned_data['available_sizes']
