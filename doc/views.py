from django.shortcuts import render
from . import DoctorModule
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'doc/docpage.html')

@csrf_exempt
def search(request):
    name = request.POST.get("name")
    print("Works")
    contextSend = DoctorModule.doc_select(name)
    if name:
        image_name = "".join(list(name.split(" ")))+".png"
        contextSend["image"]=image_name
    return render(request, 'doc/docpage.html', contextSend)

@csrf_exempt
def dept(request, id):
    context = DoctorModule.dept_select(2, int(id))
    return render(request, 'doc/dept.html', {'context':context})

@csrf_exempt
def deptpage(request, id):
    context = DoctorModule.dept_select(int(id), 0)
    print(context)
    return render(request, 'doc/deptpage.html', {'context':context})

@csrf_exempt
def about(request):
    return render(request, "doc/about.html")
