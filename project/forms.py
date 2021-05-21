from django import forms

from .models import Ap

class APForm(forms.ModelForm):

    class Meta:
        model = Ap
        fields = ('x_coord', 'y_coord', 'azimuth', 'downtilt',)
        widgets = {
            'x_coord': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'y_coord': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            # 'z_coord': forms.TextInput(
            #     attrs={'class': 'form-control'}
            # ),
            'azimuth': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'downtilt': forms.TextInput(
                attrs={'class': 'form-control'}
            )
        }