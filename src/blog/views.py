from django.shortcuts import render

from django.views.generic import (
		CreateView,
		ListView,
		DetailView,
		UpdateView,
		DeleteView
	)

from .models import Article
from .forms import ArticleForm

# Create your views here.
class ArticleListView(ListView):
	template_name = "blog/list.html"
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = "blog/detail.html"
	queryset = Article.objects.all()

class ArticleCreateView(CreateView):
	template_name = "blog/create.html"
	queryset = Article.objects.all()
	form_class = ArticleForm
	success_url = "../" 

class ArticleUpdateView(UpdateView):
	template_name = "blog/edit.html"
	queryset = Article.objects.all()
	form_class = ArticleForm
	success_url = "../../"	

class ArticleDeleteView(DeleteView):
	template_name = "blog/delete.html"
	queryset = Article.objects.all()
	success_url = "../../"

