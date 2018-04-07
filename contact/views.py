from contact.forms import ContactForm
from django.views.generic.edit import FormView
from home.views import CustomView
from django.shortcuts import render

class ContactView(CustomView, FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact/thankyou'

    def form_valid(self, form):
        form.send_email(self.request.POST)
        return super().form_valid(form)

    def get_more_context(self):
        return {'title': 'Contact'}

def thankyou(request):
    return render(request, "contact/thankyou.html")
