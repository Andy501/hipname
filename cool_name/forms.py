from django import forms




#for unauthed users
class Any_Cool_Form(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)


class CoolForm_Db(forms.ModelForm):
    name = forms.CharField(label="Your Name", max_length=100)