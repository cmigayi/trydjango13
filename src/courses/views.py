from django.shortcuts import render, get_object_or_404, redirect

from django.views import View 

from .models import Course
from .forms import CourseForm

# Create your views here.
class CourseView(View):
	template_name = "courses/list.html"
	context = {}
	obj = None

	def get(self, request, id=None, *args, **kwargs):
		self.obj = Course.objects.all()
		if id is not None:
			self.obj = get_object_or_404(Course, id=id)
		self.context["object"] = self.obj
		return render(request, self.template_name, self.context)

class CourseCreateView(View):
	template_name = "courses/create.html"
	context = {}
	obj = None

	def get(self, request, *args, **kwargs):
		form = CourseForm()
		self.context["form"] = form 	
		return render(request, self.template_name, self.context)

	def post(self, request, *args, **kwargs):
		form = CourseForm(request.POST or None)
		if form.is_valid():
			form.save()
			form = CourseForm()
		self.context["form"] = form 	
		return render(request, self.template_name, self.context)	

class CourseUpdateView(View):
	template_name = "courses/edit.html"
	context = {}
	obj = None
	form = None

	def get(self, request, id, *args, **kwargs):
		self.obj = get_object_or_404(Course, id=id)	
		self.form = CourseForm(request.POST or None, instance=self.obj)
		self.context["form"] = self.form
		return render(request, self.template_name, self.context)

	def post(self, request, id, *args, **kwargs):
		self.obj = get_object_or_404(Course, id=id)
		self.form = CourseForm(request.POST or None, instance=self.obj)
		if self.form.is_valid():
			self.form.save()
			return redirect("../../")
		self.context["form"] = self.form
		return render(request, self.template_name, self.context)
		
class CourseDeleteView(View):
	template_name = "courses/delete.html"
	context = {}
	obj = None

	def get_object(self):
		id = self.kwargs.get('id')
		if id is not None:
			self.obj = Course.objects.get(id=id)
		return self.obj

	def get(self, request, id, *args, **kwargs):
		self.obj = self.get_object()
		self.context["object"] = self.obj
		return render(request, self.template_name, self.context)	

	def post(self, request, id, *args, **kwargs):
		self.obj = self.get_object()
		if request.method == "POST":
			self.obj.delete()
			return redirect("../../")
		self.context["object"] = self.obj
		return render(request, self.template_name, self.context)	



