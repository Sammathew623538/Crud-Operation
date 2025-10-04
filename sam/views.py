from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.





def pro(request):
    products=Product.objects.all()
    return render(request,'pro.html',{'pro':products})




def add(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(pro)
    else:
        form=ProductForm()  
    return render(request,'add.html',{'form':form})  



def edit(request, id):
    product = Product.objects.get(id=id)  # product always available

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(pro)   # redirect back to product list
    else:
        form = ProductForm(instance=product)

    return render(request, 'editpro.html', {'form': form, 'product': product})

   
   
   
   
def  deletes(request,pid):
    proo=Product.objects.get(id=pid)
    if request.method =='POST':
        proo.delete()
        return redirect(pro)    
      
    return render(request,'del.html',{'pro':proo})
