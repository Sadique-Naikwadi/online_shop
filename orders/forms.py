from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'
    
