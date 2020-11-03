from django import forms
from .models import Empresas

class EmpresasForm(forms.ModelForm):
    class Meta:
        

        model = Empresas
        
        fields = [
            'name' ,
            'contract_pack' ,
            'contract_value' ,
            'cnpj' ,
            'owner' ,
            'start_data',
            'end_contract',
            'excedent',
            'service_level',
            'it_respon'
        ]
        



    
