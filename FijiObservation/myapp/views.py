from django.shortcuts import render
from .useruploadForm import UserForm
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
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
    return render(request, 'upload_file.html', {'form': form})

def fileUploadSuccess(request):
    return render(request,'index.html')