from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=100, label='password')


def contact(request):
    submitted = False

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'accounts/contact.html', {'form': form, 'submitted': submitted})
    # return render(request, "accounts/login.html", context) 
