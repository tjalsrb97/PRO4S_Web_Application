from django import forms

from .models import Ap

class APForm(forms.ModelForm):

    class Meta:
        model = Ap
        fields = ('x_coord', 'y_coord', 'z_coord', 'azimuth', 'downtilt',)