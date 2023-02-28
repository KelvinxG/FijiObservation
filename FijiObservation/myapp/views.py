from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.views import View

from .forms import UserForm
from .models import Parameter,Observation,Station,FileUpload
from django.contrib import messages
import pandas as pd
import csv
# Create your views here.


class IndexView(View):
    def get(self,request):
        #validate the form
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                #read the file from request
                file = request.FILES['file']
                read_file=file.read()
                print(read_file)

                #display a message after the file is successfully uploaded

                
                #decoded_file
                decoded_file=file.read().decode('utf-8').splitlines()
                created_file=FileUpload.objects.create(file=file) #FileUpload Model

                #save the uploaded file to the database #FileUpload model saved
                created_file.save()
                
                        
                messages.success(request, 'File uploaded successfully')
                
                return redirect('/')
            
                '''
                after read the csv file or xls
                then dump the file into the database
                '''

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
        file_dict={} #create an empty dict
        
        for filename,file in request.FILES.items():
            file_dict[filename] = file
        files=FileUpload.objects.all()
        # return render(request, 'index.html', {'form': form,'files':files})

        #get the csv and dump into json or dictionary in python

        
        return render(request,'index.html',{'form':form,'files':files,'file_dict':file_dict})

def visualizer(request, **kwargs):
    context={'data':'test'}
    return render(request, 'visualization.html',context=context)

def aboutauthor(request, **kwargs):
    return render(request,'aboutauthor.html')

def solutions(request, **kwargs):
    return render(request,'solutions.html')

def contact(request, **kwargs):
    return render(request,'contact.html')
