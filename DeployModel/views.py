from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
     return render(request,'home.html')



def result(request):

     cls=joblib.load('model.joblib')

     l=[]
     l.append(int(request.GET['YrSold']))
     l.append(int(request.GET['LotArea']))
     l.append(int(request.GET['MoSold']))
     l.append(int(request.GET['BedroomAbvGr']))
     # l=[2010,11622,2]
     
     ans=cls.predict([l])
     

     return render(request,'result.html',{'ans':ans,'l':l})

def about(request):
     return render(request,'about.html')