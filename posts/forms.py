from django.forms import ModelForm, Textarea
from .models import Post, Comment


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


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
