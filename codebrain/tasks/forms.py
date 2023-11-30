from .models import Comment
from django import forms


class AddCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'task-comment-input',
        'rows': '7',
        'cols': '54',
        'placeholder': 'Введите комментарий...',
    }), label='')

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
