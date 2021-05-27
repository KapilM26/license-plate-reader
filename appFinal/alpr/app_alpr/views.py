import os
import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.conf import settings
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from PIL import Image
from .preproc import preproc
from .predict import predict
from .ocr import ocr

from .models import Appdata
from django.http import JsonResponse
from .forms import AppForm, CreateUserForm

from rest_framework import serializers, status, viewsets
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import appSerializer

# Create your views here.

class appView(viewsets.ModelViewSet):
    serializer_class = appSerializer
    queryset = Appdata.objects.all()

def registerPage(request): 
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user )
            
            return redirect('login')


    context = {'form':form}
    return render(request,'register.html', context)

def loginPage(request):
    context ={}
    return render(request, 'login.html', context)

#remove after creation of database

class Index(APIView):
 #for displaying offender detail
    template_name = 'index.html'
    def get(self,request):
        return render(request, self.template_name,{})

    def post(self,request):
        image = request.FILES['img']
        ext = image.name.split('.')[-1]
        img_name = "img."+ext
        for filename in os.listdir(settings.IMAGE_ROOT):
            os.remove(os.path.join(settings.IMAGE_ROOT,filename))
        for filename in os.listdir(settings.PRED_ROOT):
            os.remove(os.path.join(settings.PRED_ROOT,filename))
        for filename in os.listdir(settings.PREPROC_ROOT):
            os.remove(os.path.join(settings.PREPROC_ROOT,filename))
        with open(os.path.join(settings.IMAGE_ROOT,'img.'+str(ext)), 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)
        
        predict(src_folder=settings.IMAGE_ROOT, dest_folder=settings.PRED_ROOT, model_folder=settings.MODELS_ROOT)
        
        preproc(src_folder=settings.PRED_ROOT, dest_folder=settings.PREPROC_ROOT) #preprocess output

        no = ocr(src_folder=settings.PREPROC_ROOT)
        context = {'up':os.path.join(settings.IMAGE_URL,'img.'+str(ext)),
                    'pred':os.path.join(settings.PRED_URL,"pred.png"),
                    'preproc':os.path.join(settings.PREPROC_URL,"preproc.png"),
                    'no':no}
        #print("This is working")
        #print(type(no))
        
        q=Appdata.objects.filter(vehicleNumber = "MH12QF0598") #replace with 'no'
        print(q)
        if not q:
           print("no element found in dataset")
        else:
            print(q[0].name)
            print(q[0].email)

        # print("this is working")
        # print(type(q))
        # print(q)

        return render(request, self.template_name, context)
    

        


        


