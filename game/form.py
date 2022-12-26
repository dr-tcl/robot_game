from django import forms


class RobotFormItem(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()


class DinosaurFormItem(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
