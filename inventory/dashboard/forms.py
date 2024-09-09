from django import forms
from .models import Inventory, Order, Request, Culture

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InventoryForm,self).__init__(*args, **kwargs)
        self.fields['storage'].required = False
        self.fields['receivedBy'].required = False
        self.fields['receivedBy'].label = 'Received By'

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        self.fields['staff'].label = 'Ordered By'
        
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name','quantity', 'catelogNumber', 'vendor', 'link')
    def __init__(self, *args, **kwargs):
        super(RequestForm,self).__init__(*args, **kwargs)
        self.fields['catelogNumber'].label = 'Catelog Number'

class CultureCollectionForm(forms.ModelForm):
    class Meta:
        model = Culture
        fields = '__all__'
        widgets = {
            'ReceivedDate': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CultureCollectionForm, self).__init__(*args, **kwargs)
        optional_fields = ['description', 'isolationSource', 'alternateDesignation', 'originallyReceivedFrom', 'additionalInfo']
        for field in optional_fields:
            self.fields[field].required = False
