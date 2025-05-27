from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def AboutView(request):

    # Check for posting of new comment
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Contact message submitted'
            )

    contact_form = ContactForm()
    return render(
        request,
        "about/about.html",
        {
            "contact_form": contact_form
        }
    )
