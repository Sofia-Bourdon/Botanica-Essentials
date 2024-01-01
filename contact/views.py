from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(
                request, 'Your message has been sent successfully!')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_us.html', {'form': form})
