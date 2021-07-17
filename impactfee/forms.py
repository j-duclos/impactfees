from django import forms
from django.forms.models import ModelChoiceField
from .models import *


class ServiceAreaCalculatorForm(forms.ModelForm):
    class Meta:
        model = ServiceAreaCalculator
        fields = ['service_area', 'use_type', 'use_sub_type', 'units', 'square_feet']
        labels = {
            'square_feet': "Enter Size of Individual Residential Unit (square feet):",
            'units': "Enter Number of Residential units to be built:",
        }
        use_sub_type = ModelChoiceField(UseSubType.objects.all(), empty_label=None)
        use_type = ModelChoiceField(UseType.objects.all(), empty_label=None)
        service_area = ModelChoiceField(ServiceArea.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['use_sub_type'].empty_label = None
        self.fields['use_type'].empty_label = None
        self.fields['service_area'].empty_label = None

        # Not used anymore
    ''' self.fields['use_sub_type'].queryset = UseSubType.objects.none()

        if 'use_type' in self.data:
            try:
                type_id = int(self.data.get('use_type'))
                self.fields['use_sub_type'].queryset = UseSubType.objects.filter(type_id=type_id).order_by('id')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['use_sub_type'].queryset = self.instance.use_type.use_sub_type_set.order_by('id') '''