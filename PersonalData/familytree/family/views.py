from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Family
from .models import Child
from .forms import FamilyData
from .models import Tree

# Create your views here.

def tree(request):
    fam = Tree.objects.all()
    return render(request,'tree.html',{'families':fam})

def home(request):
    fam = Family.objects.all()
    return render(request,'home.html',{'family':fam})

def fam_detail(request,id):
    identity = []
    try:
        fam = Family.objects.get(id=id)
        childarray = list(Child.objects.all().filter(parentid=id))
        child_id_dict = []
        for child in childarray:
            child_object = Family.objects.get(name=child.childid)
            child_id_dict.append(child_object)
        # print(childarray)

        try:
            spouse = Family.objects.get(name=fam.spousename)
            spouseval = spouse.id
        except:
            spouseval=0
    except fam.DoesNotExist:
        raise Http404('Object not found')
    return render(request,'fam_detail.html',{'family':fam,'spouseid':spouseval,'images':fam.otherimages.split(','),'children':child_id_dict})

def acknowledgement(request):
    if request.method=='POST':
        filled_form = FamilyData(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
            print(filled_form.cleaned_data['name'])
            print(filled_form.cleaned_data['sex'])
            new_form = FamilyData()
            return render(request,'acknowledgement.html',{'familydata':new_form,'note':note})
    else:
        note = "Enter New Information"
        form = FamilyData()
        return render(request,'acknowledgement.html',{'familydata':form,'note':note})

def edit_database(request, id):
    note = "Edit the Following Information"
    print(note)
    print(type(id))
    member = Family.objects.get(id=id)
    form = FamilyData(instance=member)
    if request.method=='POST':
        filled_form = FamilyData(request.POST,instance = member)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
    return render(request, 'edit.html', {'familydata': form, 'note': note, 'member':member})

def edit_data(request):
    if request.method == 'POST':
        note = "Edit the Following Information"
        id = request.POST.get("ID","")
        member = Family.objects.get(id=id)
        form = FamilyData(instance=member)
        return render(request, 'edit.html', {'familydata': form, 'note': note, 'member': member})
    else:
        note = "Please Enter the id of the member to be edited"
        return render(request, 'editdata.html', {'note': note})