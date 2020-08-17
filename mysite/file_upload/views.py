from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import File
from .formas import FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat

# Create your views here.


# Upload File with ModelForm
def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/file/")
    else:
        form = FileUploadModelForm()

    return render(request, 'file_uplates/upload_form.html', {'form': form,
                                                            'heading': 'Upload files with Model'})