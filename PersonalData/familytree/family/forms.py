from django import forms
from .models import Family

class FamilyData(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name','email_address','birthplace','residence','spousename','sex','age','linkimage','otherimages']