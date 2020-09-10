from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.


# def index(request):
#     return render(request,'helloworld/index.html',{})

class IndexView(TemplateView):

    template_name = 'helloworld/index.html'

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        print("{}".format(context.items()))
        context['test'] = "Lakshmi"
        return context


class SampleView(View):
    data = "Hello we are using class based views"

    def get(self,request):
        return HttpResponse(self.data)
