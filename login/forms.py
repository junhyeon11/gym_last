from django import forms

class LoginForm(forms.Form):
    id = forms.CharField(label='ID', max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), required=True)


class RegisterForm(forms.Form):
    id = forms.CharField(label='아이디', max_length=100, required=True)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(), required=True)
    passwordcheck = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(label='이메일', max_length=254, required=True)
    name = forms.CharField(label='이름', max_length=100, required=True)