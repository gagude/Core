from django import forms
from django.db.models.fields.files import ImageField
from .models import Event, Resposta
from django.forms import ClearableFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden, Field

        
class AddEvento(forms.ModelForm):
    fields = []
    def __init__(self, *args, **kwargs):
        super(AddEvento, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Event
        exclude = ('',)
        
            
class AddResposta(forms.ModelForm):
    fields = []

    def __init__(self, *args, **kwargs):
        super(AddResposta, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Resposta
        exclude = ('',)
        