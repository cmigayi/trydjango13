from django.urls import path

from .views import (
		ArticleListView,
		ArticleCreateView,
		ArticleDetailView,
		ArticleUpdateView,
		ArticleDeleteView
	)

urlpatterns = [
	path('', ArticleListView.as_view(), name='list'),
	path('create/', ArticleCreateView.as_view(), name='create'),
	path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
	path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]