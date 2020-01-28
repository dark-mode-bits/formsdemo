from django import forms
class EmployeeForm(forms.Form):
    name = forms.CharField(label="UserName")
    age = forms.IntegerField(label="Age",max_value=60,min_value=18)
    contact_no=forms.IntegerField(label="Contact No.")
    email = forms.EmailField(label="Email ID")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    re_password= forms.CharField(label="Re Enter Password",widget=forms.PasswordInput)