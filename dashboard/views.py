from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
   return render(request,'index.html',{})

def ecommerce_report_page(request):
   return render(request, 'retail_report.html', {})


def marketing_report_page(request):
   return render(request, 'marketing_report.html', {})

def about_page(request):
   return render(request,'about',{})