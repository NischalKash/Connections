from django import forms
from .models import Family, Child, Tree

class FamilyData(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['familyid','name','email_address','birthplace','residence','spousename','sex','age','linkimage','otherimages']

class Data(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['parentid','childid']