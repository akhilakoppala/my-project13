from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':123,'b':120}

    return render(request,'operations.html',context=d)
