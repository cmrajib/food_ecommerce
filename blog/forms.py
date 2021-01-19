from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]


# Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control w-100'
        # self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Save', css_class='genric-btn success circle'))

