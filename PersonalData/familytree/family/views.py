from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Family
from .models import Child
from .forms import FamilyData, Data, FamilyEntry
from .models import Tree

# Create your views here.

def tree(request):
    fam = Tree.objects.all()
    return render(request,'tree.html',{'family':fam})

def home(request, id):
    fam = Family.objects.filter(familyid = id)
    idval = Tree.objects.filter(familyid=id)
    for i in idval:
        a = i.familyname
        b = i.email_address
        c = i.linkingimage
    return render(request,'home.html',{'family':fam,'id':a,'email':b,'link':c})

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
            father = Family.objects.get(name=fam.fathername)
            fatherval = father.id
        except:
            fatherval = 0
        try:
            mother = Family.objects.get(name=fam.mothername)
            motherval = mother.id
        except:
            motherval = 0

        try:
            spouse = Family.objects.get(name=fam.spousename)
            spouseval = spouse.id
        except:
            spouseval=0
    except fam.DoesNotExist:
        raise Http404('Object not found')
    return render(request,'fam_detail.html',{'family':fam,'spouseid':spouseval,'images':fam.otherimages.split(','),'children':child_id_dict,'fatherid':fatherval,'motherid':motherval})

def childentry(request):
    if request.method == 'POST':
        filled_form = Data(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
            new_form = Data()
            return render(request, 'childentry.html', {'familydata': new_form, 'note': note})
    else:
        note = "Enter New Information"
        form = Data()
        return render(request,'acknowledgement.html',{'familydata':form,'note':note})

def familyentry(request):
    if request.method=='POST':
        filled_form = FamilyEntry(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
            new_form = FamilyEntry()
            return render(request, 'newfamily.html', {'familydata': new_form, 'note': note})
    else:
        note = "Enter New Information"
        form = FamilyEntry()
        return render(request, 'newfamily.html', {'familydata': form, 'note': note})

def authenticate(request):
    if request.method=='POST':
        login = request.POST.get("loginname", "")
        pwd = request.POST.get("password", "")
        try:
            member = Tree.objects.get(loginname=login)
        except:
            note = "Please enter valid credentials"
            return render(request, 'authenticate.html', {'note': note})

        if member.password!=pwd:
            note = "Password Mismatch"
            return render(request, 'authenticate.html', {'note': note})
        else:
            note = "Enter New Member's Information"
            form = FamilyData()
            return render(request, 'acknowledgement.html', {'familydata': form, 'note': note})
    else:
        note = "Please Enter the login credentials"
        return render(request, 'authenticate.html', {'note': note})

def acknowledgement(request):
    if request.method=='POST':
        filled_form = FamilyData(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
            new_form = FamilyData()
            return render(request,'acknowledgement.html',{'familydata':new_form,'note':note})

def edit_database(request, id):
    note = "Edit the Following Information"
    member = Family.objects.get(id=id)
    form = FamilyData(instance=member)
    if request.method=='POST':
        filled_form = FamilyData(request.POST,instance = member)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
    return render(request, 'edit.html', {'familydata': form, 'note': note, 'member':member})

def treeedit_database(request, id):
    note = "Edit the Following Information"
    member = Tree.objects.get(familyid=id)
    form = FamilyEntry(instance=member)
    if request.method == 'POST':
        filled_form = FamilyEntry(request.POST, instance=member)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thank You for Entering Information"
    return render(request, 'treeedit.html', {'familydata': form, 'note': note, 'member': member})

def treeedit(request):
    if request.method=='POST':
        note = "Edit the Following Information"
        login = request.POST.get("loginname", "")
        pwd = request.POST.get("password", "")
        member = Tree.objects.get(loginname=login)
        if member.password!=pwd:
            note = "Please enter Valid Credentials"
            return render(request, 'treeeditdata.html', {'note': note})
        else:
            form = FamilyEntry(instance=member)
            return render(request, 'treeedit.html', {'familydata': form, 'note': note, 'member': member})
    else:
        note = "Please Enter the login credentials"
        return render(request, 'treeeditdata.html', {'note': note})

def edit_data(request):
    if request.method == 'POST':
        note = "Update the following fields!!"
        globalid = request.POST.get("globalid","")
        login = request.POST.get("loginname", "")
        pwd = request.POST.get("password", "")
        try:
            member = Family.objects.get(globalid=globalid)
        except:
            note = "Please enter valid globalid"
            return render(request, 'update.html', {'note': note})

        try:
            dummy_mem = Tree.objects.get(familyid = member.familyid.familyid)
        except:
            note = "Please enter valid Family ID"
            return render(request, 'update.html', {'note': note})

        try:
            member2 = Tree.objects.get(loginname=login)
        except:
            note = "Please enter valid login name"
            return render(request, 'update.html', {'note': note})

        if member2.password != pwd:
            note = "Please enter valid credentials"
            return render(request, 'update.html', {'note': note})
        if dummy_mem.loginname!=login:
            note = "This database cannot be updated by you. Please check the ID and enter the credentials again."
            return render(request, 'update.html', {'note': note})

        form = FamilyData(instance=member)
        return render(request, 'edit.html', {'familydata': form, 'note': note, 'member': member})
    else:
        note = "Please enter the credentials"
        return render(request, 'update.html', {'note': note})

def checklink(a,b,c):
    if a == b:
        return 1
    if a not in c:
        c.append(a)
        if a=="Void" or a=="void":
            return 0
        inputdata = Family.objects.get(name=a)
        if inputdata is None:
            return 0
        x = checklink(inputdata.fathername,b,c)
        if x==1:
            return 1
        y = checklink(inputdata.mothername,b,c)
        if y==1:
            return 1
        z = checklink(inputdata.spousename,b,c)
        if z==1:
            return 1
        childarray = list(Child.objects.all().filter(parentid=inputdata.id))
        child_id_dict = []
        for child in childarray:
            child_object = Family.objects.get(name=child.childid)
            child_id_dict.append(child_object)
        for i in child_id_dict:
            f = checklink(i.name,b,c)
            if f==1:
                return 1
        return 0
    if a in c:
        return 0

def connection(request):
    if request.method == 'POST':
        first_name = request.POST.get("First_Person","")
        second_name = request.POST.get("Second_Person", "")
        output_value = checklink(first_name,second_name,[])
        print(output_value)
        if output_value==1:
            note = "The two members are connected"
            return render(request,'connected.html',{'note':note})
        else:
            note = "The two members are not connected"
            return render(request, 'notconnected.html',{'note':note})
    else:
        note = "Please enter the two names who's connection has to be checked"
        return render(request, 'connection.html',{'note':note})

def new(request):
    note = "Kindly Select the database to which new entries has to be made"
    return render(request,'new.html',{'note':note})

def newedit(request):
    note = "Kindly Select the database to which entries has to be edited"
    return render(request,'newedit.html',{'note':note})

def childedit(request):
    note = "Kindly Enter the two entities"


def delete(request):
    if request.method=='POST':
        note = "Deletion Successful. Please enter ID to be deleted"
        id = request.POST.get("ID", "")
        instance = Family.objects.get(id=id)
        instance.delete()
        return render(request, 'deletedata.html', {'note': note})
    else:
        note = "Please Enter the id of the member to be deleted"
        return render(request, 'deletedata.html', {'note': note})
def displaytree(a,b,c):
    if b not in c and b!="Void" and b!="void":
        c.append(b)
        inputdata = Family.objects.get(name=b)
        a.append(inputdata)
        displaytree(a,inputdata.spousename,c)
        childarray = list(Child.objects.all().filter(parentid=inputdata.id))
        child_id_dict = []
        for child in childarray:
            child_object = Family.objects.get(name=child.childid)
            child_id_dict.append(child_object)
        for i in child_id_dict:
            displaytree(a,i.name,c)


def display(request):
    if request.method=='POST':
        note = "The Family Tree and the persons successor is as follows : "
        id = request.POST.get("ID", "")
        member = Family.objects.get(id=id)
        newarray = []
        addarray = []
        displaytree(newarray,member.name,addarray)
        print(newarray)
        return render(request, 'displaytree.html', {'note': note,'family':newarray})
    else:
        note = "Please Enter the ID of the Person whos Family Tree has to be displayed"
        return render(request, 'retreive.html', {'note': note})

def displayfamily(request ,id):
    note = "The Family Tree and the persons successor is as follows : "
    member = Family.objects.get(id=id)
    newarray = []
    addarray = []
    displaytree(newarray, member.name, addarray)
    print(newarray)
    return render(request, 'displaytree.html', {'note': note, 'family': newarray})
