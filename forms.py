from django import forms
from .models import Mydo

class MydoForm(forms.ModelForm):
	class Meta:
		model=Mydo
		fields="__all__"