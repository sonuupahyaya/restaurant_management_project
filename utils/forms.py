from django import forms
from utils.validation_utils import is_valid_email

class UserForm(forms.Form):
    email = forms.EmailField()

        def clean_email(self):
                email = self.cleaned_data.get("email")
                        if not is_valid_email(email):
                                    raise forms.ValidationError("Invalid email format.")
                                            return email
                                            