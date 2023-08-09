from django.shortcuts import render,HttpResponseRedirect
from.forms import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})
    
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

def CandidateView(request,pk):
    candidate=Resume.objects.get(id=pk)
    # print(pk)
    return render(request,'myapp/candidate.html',{'candidate':candidate})