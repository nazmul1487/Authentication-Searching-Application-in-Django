from django import forms


class SearchForm(forms.Form):
    inputValue = forms.CharField(max_length=200)
    searchValue = forms.CharField(max_length=50)
