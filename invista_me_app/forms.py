from django.forms import ModelForm
from .models import Investimento

# cria um formulario
class InvestimentoForm(ModelForm):
    class Meta: 
        model = Investimento
        fields = '__all__'