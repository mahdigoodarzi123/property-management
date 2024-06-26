from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'group', 'description', 'location', 'floor', 'status', 'census_1403', 'room', 'user', 'vendor', 'notes']
        labels = {
            'code': 'کد اموال',
            'group': 'گروه',
            'description': 'شرح',
            'location': 'محل',
            'floor': 'طبقه',
            'status': 'وضعیت',
            'census_1403': 'سرشماری 1403',
            'room': 'اتاق',
            'user': 'استفاده کننده',
            'vendor': 'فروشنده',
            'notes': 'توضیحات',
            'assigned_user': 'یوزر اختصاص داده شده',
            
        }
