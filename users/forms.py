from django import forms
from users.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text','title']
        widgets = {
            
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details'})
        }
        