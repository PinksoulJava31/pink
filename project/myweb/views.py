from django.shortcuts import render
from . models import product
from . forms import ProductForm
from django.contrib import messages
# Create your views here.
def homepage(request):
    return render(request=request,template_name='homepage.html')

def about(request):
    return render(request=request,template_name='about.html')

def logout(request):
    return render(request=request,template_name='homepage.html')


def productview(request):
    if request.method=='POST':
       Product_Form=ProductForm(request.POST,request.FILES)
       if Product_Form.is_valid():
            Product_Form.save()
            messages.success(request,('your product is succsesfully'))
       else:
            messages.error(request,('your product is '))
    Product_Form=ProductForm()
    return render(request=request,template_name="productview.html",context={'Product_Form':Product_Form})

def Productlist(request):
    products=product.objects.all()
    return render(request=request,template_name='productlist.html',context={'products':products})

