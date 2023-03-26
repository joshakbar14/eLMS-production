from django.shortcuts import redirect, render
from django.conf import settings
from django import forms
from django.core.mail import send_mail

# Create your views here.
class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            field.label = ''

    class Meta:
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-1', 'id': 'title', 'name': 'title', 'placeholder': 'Title'}),
            'email': forms.EmailField(),
            'subject': forms.CharField(max_length=255),
            'message': forms.CharField(widget=forms.Textarea),
        }

def homepage(request):
    return render(request, 'landing_page.html')

def login(request):
    return render(request, 'login_page.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

        message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            return render(request, 'success.html')

        except Exception as e:
            
            print(f"Error sending email: {e}")

            
            return render(request, 'error.html')

    else:
        form = ContactForm()

    return render(request, 'landing_page.html', {'form': form})    