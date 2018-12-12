from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from post import models
from post.forms import CommentForm
from django.contrib import auth
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostsListView(ListView):
    template_name = 'post/post_title_list.html'
    context_object_name = 'posts'
 
    def get_queryset(self):
        posts = models.Post.objects.all().select_related('category')
        paginator = Paginator(posts, 2)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return posts

class PostDetailView(DetailView):
    template_name = 'post/detail.html'
    model = models.Post

def post_detail(request, pk):
    post = get_object_or_404( models.Post, pk=pk)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = auth.get_user(request)
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(
        request, 
        'post/detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_form': comment_form
        }
    )

def post_search(request):
    sr = request.GET.get('sr')
    if sr:
        post_list = models.Post.objects.filter(text__icontains=sr)
    return render(
        request, 
        'post/search.html',
        {
            'post_lst': post_list
        }
    )   

class SciencePostsListView(ListView):
    template_name = 'post/sc_post_title_list.html'
    queryset = models.Post.objects.filter(category=1).select_related('category')

class TechnologiesPostsListView(ListView):
    template_name = 'post/tch_post_title_list.html'
    queryset = models.Post.objects.filter(category=2).select_related('category')