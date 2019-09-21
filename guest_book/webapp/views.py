from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import NoteForm
from webapp.models import Note

def index_views(request, *args, **kwargs):
    notes = Note.objects.filter(status="active").order_by('-created_at')
    return render(request, 'index.html', context={'notes': notes})

def note_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = NoteForm()
        return render(request,'note_create.html', context={'form': form})
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Note.objects.create(name=data['name'], mail=data['mail'], text=data['text'])
            return redirect('index')
        else:
            return render(request, 'note_create.html', context={'form':form})

def note_update_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(data={'name': note.name, 'mail': note.mail, 'text':note.text})
        return render(request, 'update.html', context={'form': form, 'note': note})
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            note.name = data['name']
            note.mail = data['mail']
            note.text = data['text']
            note.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'note': note})