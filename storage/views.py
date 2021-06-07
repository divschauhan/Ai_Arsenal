from django.contrib.messages.api import info
from django.shortcuts import render, redirect, HttpResponse
from .models import AiModel, ReviewAiModel
from .forms import ModelUploadForm, ReviewUploadForm, ModelEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.core.paginator import Paginator
import mimetypes
import os
 


# Create your views here.
@login_required
def upload_form(request):
    if request.method=='POST':
        filled_form = ModelUploadForm(request.POST,request.FILES)
        if filled_form.is_valid():
            dt=filled_form.save(commit=False)
            dt.user=request.user
            dt.save()
            messages.add_message(request,messages.SUCCESS,'AI Model details uploaded successfully.')
            return redirect(to='view_model')
        else:
            messages.add_message(request,messages.ERROR,'Details are invalid, please check.')
            ctx= {'uploadform':filled_form}
            return render(request,'storage/add.html',ctx)
    if request.method=='GET':
        form = ModelUploadForm()
    return render(request,'storage/add.html',{'uploadform':form})



@login_required
def review_form(request,pk):
    result = AiModel.objects.get(pk=pk)
    info= ReviewAiModel.objects.filter(reviewer__id=request.user.id,aimodel__id=result.id)
    print(info)
   
        
    if request.method=='POST':
        if len(info)>0:
            form_data=  ReviewUploadForm(request.POST,instance=info[0]) 
        else:
            form_data=  ReviewUploadForm(request.POST) 
        if form_data.is_valid():
            form_data = form_data.save(commit=False)
            form_data.reviewer = request.user
            form_data.aimodel=result
            # form_data.rating=result
            form_data.save()
            messages.add_message(request,messages.SUCCESS,'AI Model details uploaded successfully')
            return redirect(to='view_model')

        else:
            messages.add_message(request,messages.ERROR,'form detail are invalid ,please check')
            abc = {'reviewform':form_data,'aimodel':result}
            return render(request,'storage/review.html',abc)

        
    if request.method=='GET':
        if len(info)>0:
            form=ReviewUploadForm(instance=info[0])
        else:
            form=ReviewUploadForm()
        abc = {'reviewform':form,'aimodel':result}
        return render(request,'storage/review.html',abc)




class AiModelListView(ListView):
    model = AiModel
    template_name = "storage/view.html"
    paginate_by = 4


def view_ai_models(request):
    results= AiModel.objects.all()
    context= {'results':results}
    return render(request,'storage/view.html',context)




def query_ai_models(request):
    query = request.GET.get('q','')
    results = AiModel.objects.filter(name__contains=query)
    paginator = Paginator(results, 2)
    page_num = request.GET.get('page')
    page_obj= paginator.get_page(page_num)
    context={'result':page_obj,'query':query}
    return render(request,'storage/search.html',context)

def detail_of_ai_model(request,pk):
    result = AiModel.objects.get(pk=pk)
    reviews = ReviewAiModel.objects.filter(aimodel_id=pk)
    context={'result':result,'reviews':reviews}
    return render(request,'storage/detail.html',context)


def edit_ai_model(request,pk):
    try:
        data = AiModel.objects.get(pk=pk)
        if request.method =='POST':
            form = ModelEditForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return redirect('view_model')   
        else:
            form = ModelEditForm(instance=data)
        context ={ "editform":form}
        return render(request,'storage/edit.html',context) 
    
    except Exception as e:
        print('some error occured')
        return redirect('view_model')        
 
        

def delete_ai_model(request,pk):
    try:
        AiModel.objects.filter(pk=pk).delete()
    except:
        print('same error occured')
    return redirect('view_model')




def download_file(request):
    if request.method == "GET":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fl_path = request.GET.get('path')
        filename = os.path.basename(fl_path)
        fl = open(BASE_DIR+fl_path,'rb')
        mime_type, _ = mimetypes.guess_type(fl_path)
        response = HttpResponse(fl, content_type=mime_type)
        response['content-Disposition'] = "attachment; filename=%s" % filename
        return response
    return redirect('view_model')


