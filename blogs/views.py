from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import generic
from .models import Post

from .forms import PostForm
from django.forms import modelformset_factory

class PostList(generic.ListView):
    paginate_by = 4
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def get_name(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():    
            form.save()
            return redirect('home')
    else:
        form_class = PostForm
    return render(request, 'name.html', {'form': form_class,})

def edit(request,slug):
    if request.method == 'POST':
        edited_form = PostForm(request.POST)
        if edited_form.is_valid():
            g = Post.objects.get(slug=edited_form['slug'].value())
            if(g):
                g.title = edited_form.cleaned_data['title']
                g.slug = edited_form.cleaned_data['slug']
                g.content = edited_form.cleaned_data['content']
                g.save()
                return redirect('home')
    else:
        a = Post.objects.get(slug=slug)
        form = PostForm(instance=a)
        return render(request,'edit.html',{'form': form,'form_slug':a.slug})
