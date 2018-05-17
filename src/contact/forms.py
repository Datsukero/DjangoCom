from django import forms

class contactForm(forms.Form):
	"""docstring for contactForm"""
	nome = forms.CharField(required=False, max_length=100, help_text='maximo de 100 caracteres.')
	email = forms.EmailField(required=True)
	mensagem = forms.CharField(required=True, widget=forms.Textarea)