from django.forms import ModelForm, Textarea, TextInput
from .models import Post, Comment


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Text',
        }
        widgets = {
            'title': TextInput(attrs={'placeholder': ''}),
            'text': Textarea(attrs={'placeholder': '', 'rows': 6}),
        }


class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '',
        }
        widgets = {
            'text': Textarea(attrs={'placeholder': 'Write your opinion...', 'rows': 3}),
        }
