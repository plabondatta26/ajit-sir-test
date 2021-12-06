from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.


def create_writer(request):
    if request.method == 'POST':
        form = WriterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'create_writer.html')


def writer_list(request):
    print(request.user)
    data = WriterModel.objects.all()
    return render(request, 'writer_list.html', {'data': data})
