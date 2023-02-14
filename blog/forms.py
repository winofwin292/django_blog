from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={"class": "form-control input-mf",
                                                                                       "placeholder": "Name *"}))
    email = forms.EmailField(required=True, max_length=50,
                             widget=forms.EmailInput(attrs={"class": "form-control input-mf",
                                                            "placeholder": "Email *"}))
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control input-mf",
                                                                       "placeholder": "Comment *",
                                                                       "cols": "45", "rows": "8"}))


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Your Name *", "data-rule": "minlen:4", "data-msg": "Please enter at least 4 chars"}))
    email = forms.EmailField(required=True, max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': "Your Email *", "data-rule": "email", "data-msg": "Please enter a valid email"}))
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Message *", "rows": "5", "data-rule": "required", "data-msg": "Please write something for us"}))
