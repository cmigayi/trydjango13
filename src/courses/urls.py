from django.urls import path

from .views import (
		CourseView,
		CourseCreateView,
		CourseUpdateView,
		CourseDeleteView
	)

urlpatterns = [
	path('', CourseView.as_view(), name='list'),
	path('create/', CourseCreateView.as_view(), name='create'),
	path('<int:id>/', CourseView.as_view(template_name="courses/detail.html"), name='list'),
	path('edit/<int:id>/', CourseUpdateView.as_view(), name='edit'),
	path('delete/<int:id>/', CourseDeleteView.as_view(), name='delete'),
]