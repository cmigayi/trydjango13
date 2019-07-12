from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(
			widget = forms.TextInput(
					attrs = {
						"placeholder": "Title"
					}
				)
		)
	desc = forms.CharField(
			widget = forms.Textarea(
					attrs = {
						"placeholder": "Description"
					}
				)
		)
	price = forms.DecimalField(
			widget = forms.NumberInput(
					attrs = {
						"placeholder": "Price"
					}
				)
		)
	class Meta:
		model = Product
		fields = [
			"title",
			"desc",
			"price"
		]

	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) < 2:
			raise forms.ValidationError("Title too short!")
		return title	 	

class RawProductForm(forms.Form):
	title = forms.CharField(
			widget = forms.TextInput(
					attrs = {
						"placeholder": "Title"
					}
				)
		)
	desc = forms.CharField(
			widget = forms.Textarea(
					attrs = {
						"placeholder": "Description"
					}
				)
		)
	price = forms.DecimalField(
			widget = forms.NumberInput(
					attrs = {
						"placeholder": "Price"
					}
				)
		)			