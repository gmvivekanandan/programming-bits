from django.forms import ModelForm
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }