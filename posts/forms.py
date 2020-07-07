from django import forms
from posts.models import *

class PostForm(forms.ModelForm):
    
    class Meta:
        model = ProjectPost
        fields = ('project_name', 'project_image', 'project_description', 'project_category', 'project_url')
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'username',
        'rows': '1'
    }))
    class Meta:
        model = Comment
        fields = ('content', )
