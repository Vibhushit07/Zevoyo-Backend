from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):

    # message = forms.CharField()
    class Meta:
        model = Chat
        fields = ('message',)
