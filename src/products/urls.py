from django.urls import path

from .views import (
		product_list,
		product_detail,
		product_edit,
		product_create,
		raw_product_form,
		product_delete,
	)

app_name = "products"

urlpatterns = [
    path('', product_list, name='list'),
    path('<int:id>/', product_detail, name='detail'),
    path('edit/<int:id>/', product_edit, name='edit'),
    path('create/', product_create, name='create'),
    path('delete/<int:id>/', product_delete, name='delete'),
]