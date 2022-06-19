from django.shortcuts import render
from django import template
from .forms import AksaraForm
from .models import Aksara
import os
import io
from PIL import Image as im
import torch
import json
# Create your views here.

def AksaraView(request):
    form = AksaraForm(request.POST, request.FILES)
    if form.is_valid():
        img = request.FILES.get('gambar')
        img_instance = Aksara(
            gambar=img
        )
        img_instance.save()

        img_terbaru = Aksara.objects.filter().last()
        img_bytes = img_terbaru.gambar.read()
        img = im.open(io.BytesIO(img_bytes))


        path_hubconfig = "static/yolov5"
        path_weightfile = "static/aksara/best.pt" #hasil training
        model = torch.hub.load(path_hubconfig, 'custom', path=path_weightfile, source='local',force_reload=True)
        results = model(img, size=640)
        
        results.render()
        for img in results.imgs:
            img_base64 = im.fromarray(img)
            img_base64.save("media/yolo_out/gambar_predik.jpg", format="JPEG")

        hasil_predict_img = "/media/yolo_out/gambar_predik.jpg"
        extract = results.pandas().xyxy[0].to_json(orient='records')
        extract2 = json.loads(extract)
        form = AksaraForm()
        context = {
            "aksara": form,
            "prediksi_aksara_jawa": hasil_predict_img,
            "ekstrak":extract2,
        }
        return render(request, 'aksara/indra.html', context)

    else:
        form = AksaraForm()
    context = {
        "aksara": form
    }
    return render(request, 'aksara/indra.html', context)



