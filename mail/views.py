from mail.forms import SendMailForm
from django.views.generic.edit import FormView
from home.views import CustomView
from django.contrib.auth.mixins import LoginRequiredMixin

class SendMailView(LoginRequiredMixin, CustomView, FormView):
    template_name = 'mail/send_mail.html'
    form_class = SendMailForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email(self.request.POST)
        return super().form_valid(form)

    def get_more_context(self):
        return {'title': 'Send Mail'}

