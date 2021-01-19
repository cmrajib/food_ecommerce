from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms, TextInput

from UserRegistration.models import  User



# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user',)
#
#
# # Appling css class to the field and button
#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'single-input'
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit', 'Save', css_class='genric-btn success circle'))



class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('full_name','address_1','phone','email','password1', 'password2',)

    # Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['full_name'].widget = TextInput(attrs={
    #         'class': 'form-block',
    #         'placeholder': 'Name'})

# 'single-input'
        # self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Create Account', css_class='genric-btn success circle'))



