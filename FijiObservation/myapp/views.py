from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .forms import UserForm
from .models import Parameter,Observation,Station,FileUpload
from django.contrib import messages
import pandas as pd
# Create your views here.


def index(request):
    #validate the form
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            #read the file from request
            file = request.FILES['file']
            #display a message after the file is successfully uploaded
            created_file=FileUpload.objects.create(file=file)
            created_file.save()
            
            messages.success(request, 'File uploaded successfully')
            

            if file.name.endswith('.csv'):

                df = pd.read_csv(file)
                #read csv file and then store into database
            
                # Do something with the CSV data
            elif file.name.endswith('.xls') or file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
                # Do something with the Excel data
            else:
                form.add_error('file', 'Unsupported file format')
        else:
            form.add_error(None, 'Please select a file')
    else:
        form = UserForm()
    files=FileUpload.objects.all()
    # return render(request, 'index.html', {'form': form,'files':files})
    return redirect(request,'index.html',{'form':form,'files':files})

def visualizer(request, **kwargs):
    return render(request, 'visualization.html')