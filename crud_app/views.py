from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User

# Add data in DB and Show

#This function will ADD new items and SHOW all items
def add_show(request):

    if request.method =='POST':
        form= StudentRegistration(request.POST)
        if form.is_valid():
            # name= form.cleaned_data['name']
            # email= form.cleaned_data['email']
            # password= form.cleaned_data['password']

            # reg= User(name= name, email= email, password= password)
            # reg.save()

            # or 

            form.save()
            form= StudentRegistration() #gives the blank form after Saving Data.
            return redirect('sucess');

    else:
        form= StudentRegistration()

    stud= User.objects.all()
    return render(request, 'crud/add_and_show.html', {'form': form, 'students': stud})

#This function will Delete items
def delete_data(request, id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        return redirect('sucess')

# This function will UPDATE/Edit Data
def update_data(request, id):
    #When Clicked on EDIT= GET REQUEST and when clicked on UPDATE= POST REQUEST

    if request.method == 'POST': #(UPDATE)
        user = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('add_and_show')

    else:
        #Get Request(EDIT)
        user = User.objects.get(pk=id)
        form = StudentRegistration(instance=user)

    return render(request, 'crud/update_student.html', {'form': form})

#This function will show the Sucess Message
def sucess(request):
    return render(request, 'crud/sucess.html')