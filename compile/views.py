from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import subprocess
import re
# Create your views here.

def editor(request):
	return render(request,'compile/editor.html',)

def compile(request):
	if request.method=="POST":
		code=request.POST['code']
		f=open('./codes/code.cpp','w')
		f.seek(0)
		f.truncate()
		f.write(code)
		f.close()
		try:
			result = subprocess.check_output(["g++","./codes/code.cpp"],stderr = subprocess.STDOUT)
			subprocess.call(["g++","./codes/code.cpp"])
			result = " "
		except subprocess.CalledProcessError,e:
			result = e.output
			result = result.replace("./codes/code.cpp:","");
			has = re.match(r'\/usr.*',result)
			if(has):
				result = re.sub(r'\/usr.*','',result)
				result = re.sub(r'\s+',' ',result)
		html = render_to_string('compile/status.html',{'result':result})
		return HttpResponse(html)
		#result contains the required response
		#return render_to_response('compile/status.html',{'result':result},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/compile/editor')