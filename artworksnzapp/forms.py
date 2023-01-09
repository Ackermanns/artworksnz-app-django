from django import forms
from django.forms import ModelForm
from .models import Artwork, Artist

#NOTE: This form was used for testing purposes, form html is hard coded into the addartwork.html file now
class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'
        
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'