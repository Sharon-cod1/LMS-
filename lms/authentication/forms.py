from django import forms


class LoginForm(forms.Form):
    # use form class to create a form 

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                            'required': 'required'
                                                                            }))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'required': 'required'
                                                                                 }))
    