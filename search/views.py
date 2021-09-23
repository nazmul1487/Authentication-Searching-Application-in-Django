from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SearchForm


# Create your views here.
from .models import UserInput


class SearchView(View):

    def get(self, request, *args, **kwarg):
        search_form = SearchForm()
        return render(request, 'search.html', {"search_form": search_form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                userInput = UserInput()
                inputvalue = search_form.cleaned_data['inputValue']
                searchvalue = search_form.cleaned_data['searchValue']
                data = inputvalue.split(',')
                data = [value.strip() for value in data]
                data = sorted(data, reverse=True)
                userInput.inputValue = ', '.join(data)
                userInput.user = request.user
                userInput.save()
                message = ''
                if searchvalue in inputvalue:
                    print("found")
                    find = True
                    message = 'True'
                else:
                    print("not found")
                    find = False
                    message = 'False'
                context = {
                    'message': message,
                    'search_form': search_form,
                }
                return render(request, 'search.html', context)
        search_form = SearchForm()
        context = {
            'search_form': search_form,
        }
        return render(request, 'search.html', context)