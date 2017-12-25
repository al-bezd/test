from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from models import Test

context={}
def index(request):
    response = render(request, 'test_app/uploadtext.html', context)
    return response

def get_text(request):
    try:
        context['result']=Test.objects.all()
    except:
        context['result'] = [{'upl_text':'blank'},]
    response=render(request,'test_app/getText.html',context)
    return response

def upload_text(request):
    if request.POST.get('txt'):
        m=Test(upl_text=request.POST.get('txt'))
        m.save()
        return HttpResponseRedirect('/success')

def success(request):
    context['msg']='success'
    response = render(request, 'test_app/success.html', context)
    return response