from django import forms
import mistune

class ContactForm(forms.Form):
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def markdown(self, value):
        markdown = mistune.Markdown()
        return markdown(value)
    
    def send_email(self, fields):
        from django.core.mail import EmailMultiAlternatives
        from django.utils.html import strip_tags

        subject, from_email, to = "contact | %s" % fields["name"], 'contact_me@lukespademan.com', 'info@lukespademan.com'
        
        html_content = self.markdown(fields["message"])
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    
