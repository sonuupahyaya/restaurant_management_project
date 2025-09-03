from django.shortcuts import render
from .models import RestaurantLocation
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

# Build email content
       subject = f"New Contact Form Submission from {name}"
       full_message = f"Message from {name} ({email}):\n\n{message}"

# Send email
        send_mail(
        subject,
        full_message,
settings.DEFAULT_FROM_EMAIL,
    ['perpexrestaurant@gmail.com'],  # Restaurant email
fail_silently=False,
)

return redirect('contact_success')  # Redirect after success
else:
       form = ContactForm()

return render(request, "contact.html", {"form": form})
                                                                                                                                                                                                                                            
def home(request):
    location = RestaurantLocation.objects.first()
        context = {"location": location}
            return render(request, "home.html", context)
            