from django import forms
from .models import newstudent

# class Student(forms.Form):
#     name=forms.CharField(label='Name',widget=forms.TextInput)
#     Age = forms.CharField(label='Age', widget=forms.NumberInput)
#     Address = forms.CharField(label='Address', widget=forms.Textarea)
#     list1=[('Male','Male'),('Female','Female')]
#     gender=forms.ChoiceField(choices=list1,widget=forms.RadioSelect)
#     FRUIT_CHOICES=[
#         ('Orange','Orange'),
#         ('Apple','Apple'),
#         ('Grape','Grape'),
#         ('Kiwi','Kiwi')
#     ]
#     favorite_fruit=forms.CharField(widget=forms.Select(choices=FRUIT_CHOICES))
#     email=forms.EmailField(label='Email')
#     password=forms.CharField(label='Password',widget=forms.PasswordInput)
#     Confirmpassword = forms.CharField(label='Confirm_Password', widget=forms.PasswordInput)
#     fileupload=forms.FileField()
#
#     def clean_name(self):
#         value=self.cleaned_data['name']
#         if value.isupper():
#             raise forms.ValidationError("Please dont use upper case")
#         return value
#
#     def clean_Address(self):
#         value=self.cleaned_data['Address']
#         if value.islower():
#             raise forms.ValidationError("Please use upper case")
#         return value
#
#     # def clean_email(self):
#     #     value=self.cleaned_data['email']
#     #     # dom=value.split('@')[1]
#     #     # dom_list=["hotmail.com"]
#     #     # if dom in dom_list:
#     #     if value.endswith('hotmail.com'):
#     #         raise forms.ValidationError("Domain not accepted")
#     #     return value
#
#     # def clean_email(self):
#     #     email = self.cleaned_data.get('email')
#     #     try:
#     #         match = newstudent.objects.get(email=email)
#     #     except newstudent.DoesNotExist:
#     #         return email
#     #     raise forms.ValidationError('This email address is already in use.')
#     def clean_email(self):
#         data = self.cleaned_data['email']
#         if newstudent.objects.filter(email=data).exists():
#             raise forms.ValidationError('Your email is already in our list of users to be notified.Try a new email')
#         return data
#
#     def clean_Confirmpassword(self):
#         value1=self.cleaned_data['password']
#         value2=self.cleaned_data['Confirmpassword']
#         if value1 != value2:
#             raise forms.ValidationError("Password doesn't match")
#         return value1

# class emailnew(forms.Form):
#     from_add=forms.EmailField(label='From Email')
#     to_add=forms.EmailField(label='To Email')
#     subject=forms.CharField(label='Subject')
#     message=forms.CharField()
#     attachment=forms.FileField()

class LoginForm(forms.Form):
    username=forms.CharField(label='username')
    mail_id=forms.EmailField(label='email')
    password=forms.CharField(label='password',widget=forms.PasswordInput)


