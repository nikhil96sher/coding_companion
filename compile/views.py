from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import subprocess
# Create your views here.

def editor(request):
	return render(request,'compile/editor.html',)

def compile(request):
	code=request.POST['code']
	f=open('./codes/code.cpp','w')
	f.seek(0)
	f.truncate()
	f.write(code)
	try:
		result = subprocess.check_output(["g++","./codes/code.cpp"])
		subprocess.call(["g++","./codes/code.cpp"])
		result = ""
	except subprocess.CalledProcessError,e:
		result = e.output
	
	return render_to_response('compile/result.html',{'result':result},context_instance=RequestContext(request))