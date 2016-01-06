from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import subprocess
import re
import requests
import sys,errno
# Create your views here.

def main(request):
	return render(request,'ccr/main.html',)

def share(request):#Has to be worked on
	if request.method=="POST":
		url="http://ideone.com/ideone/Index/submit/"
		
		link = "http://ideone.com/"
		return HttpResponse(link)
	else:
		return HttpResponseRedirect('/ccr/')

def save(request):
	if request.method=="POST":
		filename = request.POST['file']
		code = request.POST['code']
		inp = request.POST['input']
		url = './codes/saved/'+filename+'.cpp'
		f = open(url,'w')
		f.seek(0)
		f.truncate()
		f.write(code)
		f.close()
		url = './codes/saved/'+filename+'.txt'
		f = open(url,'w')
		f.seek(0)
		f.truncate()
		f.write(inp)
		f.close()
		result = "Status : File Saved"
		return HttpResponse(result)
	else:
		return HttpResponseRedirect('/ccr/')

def compile(request):
	if request.method=="POST":
		code = request.POST['code']
		inp = request.POST['input']
		
		#Writing Code into the file
		f=open('./codes/code.cpp','w')
		f.seek(0)
		f.truncate()
		f.write(code)
		f.close()

		try:
			output = subprocess.check_output(["g++","./codes/code.cpp"],stderr = subprocess.STDOUT)
			subprocess.call(["g++","./codes/code.cpp"])
			result = "Compilation Successful"
		except subprocess.CalledProcessError,e:
			output = e.output
			output = output.replace("./codes/code.cpp:","");
			has = re.match(r'\/usr.*',output)
			if(has):
				output = re.sub(r'\/usr.*','',output)
				output = re.sub(r'\s+',' ',output)
			result = "Compilation Error"
		return render_to_response('ccr/status.html',{'result':result,'input':inp,'output':output},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/ccr/')

def run(request):
	if request.method=="POST":
		#code=request.POST['code']
		testcase=request.POST['input']
		
		if testcase=="":
			testcase = " "

		#f=open('./codes/code.cpp','w')
		#f.seek(0)
		#f.truncate()
		#f.write(code)
		#f.close()
		
		#try:	#Compilation Successful
		#	output = subprocess.check_output(["g++","./codes/code.cpp"],stderr = subprocess.PIPE)
		#	subprocess.call(["g++","./codes/code.cpp"])#,stderr = subprocess.PIPE)
		#	result = "Compilation Successful"
			
		try:
			inp = open('./input.txt','w')
			inp.seek(0)
			inp.truncate()
			inp.write(testcase)
			inp.close()
		except EOFError,e:
			result = "File Reading Error"
			html = render_to_string('ccr/status.html',{'result':result,'input':testcase,'output':output})
			return HttpResponse(html)



		try:	#running successful
			output = subprocess.check_output(["./a.out","<","input.txt"],stderr = subprocess.PIPE)
				#subprocess.call(["./a.out","<","input.txt"])
			result = "Execution Successful"
		except subprocess.CalledProcessError,er:	#error while running
			output = er.output
			result = "Execution Failed"
		except socket.error,e:
			result = "Socket Error"
		except IOError,e:
			if e.errno == errno.EPIPE:
				result = "EPIPE Error"
			else:
				result = "Other IOerror"

		#except subprocess.CalledProcessError,e:	#compilation failed
		#	output = e.output
		#	output = output.replace("./codes/code.cpp:","");
		#	has = re.match(r'\/usr.*',output)
		#	if(has):
		#		output = re.sub(r'\/usr.*','',output)
		#		output = re.sub(r'\s+',' ',output)
		#	result = "Compilation Error"
		#except socket.error,e:
		#	result = "Socket Error"
		#except IOError,e:
		#	if e.errno == errno.EPIPE:
		#		result = "EPIPE Error"
		#	else:
		#		result = "OTHer errror"
		html = render_to_string('ccr/status.html',{'result':result,'input':testcase,'output':output})
		return HttpResponse(html)
	else:
		return HttpResponseRedirect('/ccr/editor')