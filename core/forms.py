from django import forms
from .models import Image

class Image_Form(forms.ModelForm):
    """Form for the image model """
    class Meta:
        model = Image
        fields = ('title', 'image')