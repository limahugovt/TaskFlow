from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Digite seu email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Digite sua senha...'}))

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite seu nome...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Digite seu email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Digite sua senha...'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirme sua senha...'}))
