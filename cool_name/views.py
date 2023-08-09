from django.shortcuts import render
from .forms import Any_Cool_Form, CoolForm_Db
from .models import CoolName


#any users route no db
def MakeAnyOneNameCool(request):
     #Template controls which name is viewable, by JS Click over preloaded values
    
    if request.method == "POST":
        form = Any_Cool_Form(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            name1 = "Lil' " + name + "ington"
            name2 = "Big Boss " + name + "illini" 
            context = {"Name1":name1, "Name2": name2}
            return render(request, 'cool_name/TheNewName.html', context)
    else:
        form = Any_Cool_Form()
    
    context ={'form':form}
  
    return render(request, 'cool_name/Anyone.html', context)


#signed in users route, saves to db
def MakeMemberNameCool(request):
    #required flow, pass the user id from url and func def, filter the user, create the name, modify the created name, save to db. 
    user_instance = CoolName.objects.all()
    context = {"user":user_instance} 
    
 
    return render(request, 'cool_name/AuthName.html', context)



def ReturnedName(request):
    #where view can see their auth name cooled. 
    return render(request, 'cool_name/TheNewName.html' )