from django.shortcuts import render
from .models import products
# Create your views here.
def index(request):
    product = products.objects.all()
    param={'product':product}
    return render(request,'products/index.html',param)

