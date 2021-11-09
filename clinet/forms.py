from django import forms
from main.models import Category,Product, Kontak
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = '__all__'

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product()
		fields = "__all__"



class KontakForm(forms.ModelForm):
	class Meta:
		model = Kontak
		fields = "__all__"