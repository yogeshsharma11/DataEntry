from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout
from django.contrib import messages
from  .models import Data
from django.core.paginator import Paginator
import re
import csv

# Create your views here.

def register_view(request):
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
   else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
   return render(request, 'register.html',{'form':form})



def login_view(request):
   if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username or password.')
   else:
        form = AuthenticationForm()
   return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        country = request.POST.get('country')
        if re.fullmatch(r'\d{10}', contact):  
            Data.objects.create(name=name, contact=contact, country=country)
        else:
            messages.error(request, "Invalid mobile number. It must be 10 digits.")
            return redirect('index')

        return redirect('index')
    
    data_list = Data.objects.all()
    
    paginator = Paginator(data_list, 5) 
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    
    return render(request, 'index.html', {
        'page_obj': page_obj,
        'data_list': page_obj.object_list, 
    })

    
@login_required
def export_csv(request):
  
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data_export.csv"'
    writer = csv.writer(response)
    writer.writerow(['S.No', 'Name', 'Contact', 'Country'])

    data_list = Data.objects.all()
    for index, row in enumerate(data_list, start=1):
        writer.writerow([index, row.name, row.contact, row.country])

    return response


@login_required
def delete_data(request, data_id):

    data = get_object_or_404(Data, id=data_id)
    data.delete()
    messages.success(request, f"Data '{ data.name }' has been successfully deleted.")
    return redirect('index')


@login_required
def edit_data(request, data_id):
   
    data = get_object_or_404(Data, id=data_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        country = request.POST.get('country')

        if not re.fullmatch(r'\d{10}', contact):  
            messages.error(request, "Invalid mobile number. It must be 10 digits.")
            return redirect('edit_data', data_id=data.id)

        data.name = name
        data.contact = contact
        data.country = country
        data.save()
        messages.success(request, "Data updated successfully!")
        return redirect('index')

    return render(request, 'edit.html', {'data': data})





