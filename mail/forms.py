from django import forms
import mistune

class SendMailForm(forms.Form):
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def markdown(self, value):
        markdown = mistune.Markdown()
        return markdown(value)
    
    def send_email(self, fields):
        from django.core.mail import EmailMultiAlternatives
        from django.utils.html import strip_tags

        subject, from_email, to = fields["subject"], 'info@lukespademan.com', fields["to"]
        
        html_content = self.markdown(fields["message"])
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    
