import os
from django.shortcuts import render
from django.views import View
from django.conf import settings
from PIL import Image
from .preproc import preproc
from .predict import predict
from .ocr import ocr

# Create your views here.

class Index(View):
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
        return render(request, self.template_name, context)