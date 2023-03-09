from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from .models import Post, Category , Comment
from .forms import PostForm , EditForm , CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
"""
def home(request):
    return render(request, 'home.html',{})
"""

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu

       
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    

    

class AddPostView(CreateView):
    model = Post
    form_class= PostForm
    template_name ='add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    #fields = ['title','body']
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name ='add_category.html'
    fields= '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

def LikeView(request, pk):
    post =  get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article_details',args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name ='add_comment.html'
    

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})
 