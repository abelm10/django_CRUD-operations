from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm

def list_persons(request):
    persons = Person.objects.all()
    return render(request, 'crudoperations/list_persons.html', {'persons': persons})

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_persons')
    else:
        form = PersonForm()
    return render(request, 'crudoperations/create_person.html', {'form': form})

def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('list_persons')
    else:
        form = PersonForm(instance=person)
    return render(request, 'crudoperations/update_person.html', {'form': form})

def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('list_persons')
    return render(request, 'crudoperations/delete_person.html', {'person': person})
