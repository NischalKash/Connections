from django import forms
from .models import Family, Child, Tree, Images

class FamilyData(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['globalid','familyid','name','sex','fathername','mothername','email_address','birthplace','residence','spousename','age','linkimage']

class Data(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['parentid','childid']

class FamilyEntry(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['familyid','loginname','password','familyname','linkingimage','email_address']

class ImagesUpload(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['globalid','images']

