from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    rpassword = forms.CharField(label = "Re-enter Password", widget = forms.PasswordInput)

    def clean(self):
       cleaned_data = super().clean()
       valpwd = self.cleaned_data['password']
       valrpwd = self.cleaned_data['rpassword']
       if valpwd != valrpwd:
           raise forms.ValidationError('Enter password does not matched')
        