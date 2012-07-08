from django import forms
from models import Bookmark

class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        fields = ('creator','url','title','public')
