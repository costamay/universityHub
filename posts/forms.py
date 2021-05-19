from django import forms
from posts.models import *

class PostForm(forms.ModelForm):
    
    class Meta:
        model = ProjectPost
        fields = ('project_name', 'project_picture', 'project_description', 'project_category', 'project_url')
        
class CommentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'username',
        'rows': '1'
    }))
    class Meta:
        model = Comment
        fields = ('description', )

class AuthorUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ['profile_image']
                  
    def clean_profile_image(self):
        if self.is_valid():
            profile_image = self.cleaned_data['profile_image']
            try:
                author = Author.objects.exclude(pk=self.instance.pk).get(profile_image=profile_image)
            except Author.DoesNotExist:
                return profile_image
            raise forms.ValidationError('Profile image "%s" is already in use.' % profile_image)
