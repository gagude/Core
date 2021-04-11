from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden, Field
        
class AddUsers(forms.ModelForm):
    fields = []
    def __init__(self, *args, **kwargs):
        super(AddUsers, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Profile
        exclude = ('',)
        