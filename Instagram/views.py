from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect


class PostListView(ListView):
    model = Post
    template_name = 'index.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']

def index(request):

    posts = Post.get_all_images()
    print(posts)
    context={
        'posts':posts,
    }

    return redirect(request,'index.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name='instagram/post_form.html'
    fields = ['caption', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name='instagram/post_detail.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['caption', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/instagram'
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

def about(request):
    return render (request, 'about.html')

@login_required(login_url='/login/')
def likePost(request,image_id):

   image = Post.objects.get(pk = image_id)

   is_liked = False
   if image.likes.filter(id = request.user.id).exists():
       image.likes.remove(request.user)
       is_liked = False
   else:
       image.likes.add(request.user)
       is_liked = True

   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def search(request):
    form = SearchForm()
    return render(request, 'index.html', {'form': form})
