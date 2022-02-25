from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from . forms import AppoinmentModelForm
from.models import Appointment

def register(request):
    
    if request.method == 'POST':
        form = AppoinmentModelForm(request.POST)
        print("vhghgfj")
        if form.is_valid():

            form.save()
            users = Appointment.objects.all()
            messages.success(request, f'Your account has been created. You can log in now!')    
            # return redirect('login')
    else:
        form = AppoinmentModelForm()

    context = {'form': form}
    # print("dsfs")
    return render(request, 'appointmnet/welcome.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = AppoinmentModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Your account has been created. You can log in now!')    
#             # return redirect('login')
#     else:
#         form = AppoinmentModelForm()

#     context = {'form': form}
#     return render(request, 'doc_pat/register.html', context)

def index(request):
    form = AppoinmentModelForm()

    context = {'form': form}
    return render(request,'appointmnet/index.html',context)