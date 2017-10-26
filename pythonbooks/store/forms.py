from django import forms

class SubmitBook(forms.Form):
	item_id = forms.CharField(max_length=10)

