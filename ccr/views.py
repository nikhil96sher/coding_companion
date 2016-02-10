from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

import subprocess
import re
import os
import datetime
import hashlib
# Create your views here.

def main(request):
	time = datetime.datetime.now()
	token = hashlib.sha224(str(time)).hexdigest()
	token = token[0:8]	#Token length is 8
	return render(request,'ccr/main.html',{'token':token})

def template(request):
	try:
		f = open('./codes/saved/template.cpp','r')
		template = f.read()
	except:
		template = ""
	return HttpResponse(template)

def save(request):
	if request.method=="POST":
		filename = request.POST['file']
		code = request.POST['code']
		inp = request.POST['input']
		
		try:
			url = './codes/saved/'+filename+'.cpp'
			f = open(url,'w')
			f.seek(0)
			f.truncate()
			f.write(code)
			f.close()
		except:
			result = "Status : Sorry, can't save files at the moment"
			return HttpResponse(result)
		try:
			url = './codes/saved/'+filename+'.txt'
			f = open(url,'w')
			f.seek(0)
			f.truncate()
			f.write(inp)
			f.close()
			result = "Status : File Saved"
		except:
			result = "Status : Sorry, can't save files at the moment"
		
		return HttpResponse(result)
	else:
		return HttpResponseRedirect('/ccr/')

def compile(request):
	if request.method=="POST":
		code = request.POST['code']
		inp = request.POST['input']
		token = request.POST['uniquetoken']
		#inp = inp + '\n'
		
		#Writing Code into the file
		f=open('./codes/tmp/'+token+'.cpp','w')
		f.seek(0)
		f.truncate()
		f.write(code)
		f.close()

		#Writing Input into the file
		test = open('./codes/tmp/'+token+'.txt','w')
		test.seek(0)
		test.truncate()
		test.write(inp)
		test.close()

		try:
			output = subprocess.check_output(["g++","./codes/tmp/"+token+".cpp"],stderr = subprocess.STDOUT)
			subprocess.call(["g++","./codes/tmp/"+token+".cpp"])
			result = "Compilation Successful"
		except subprocess.CalledProcessError,e:
			output = e.output
			output = output.decode('utf-8').replace("./codes/tmp/"+token+".cpp:","");
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
		code = request.POST['code']
		inp = request.POST['input']
		token = request.POST['uniquetoken']
		
		#Writing Code into the file
		f=open('./codes/tmp/'+token+'.cpp','w')
		f.seek(0)
		f.truncate()
		f.write(code)
		f.close()
		
		#Writing testcase into file
		f = open('./codes/tmp/'+token+'.txt','w')
		f.seek(0)
		f.truncate()
		f.write(inp)
		f.close()
	
		try:	#Compilation
			output = subprocess.check_output(["g++","./codes/tmp/"+token+".cpp"],stderr = subprocess.STDOUT)
			subprocess.call(["g++","./codes/tmp/"+token+".cpp"])
			result = "Compilation Successful"
		except subprocess.CalledProcessError,e:
			output = e.output
			output = output.replace("./codes/tmp/"+token+".cpp:","");
			has = re.match(r'\/usr.*',output)
			if(has):
				output = re.sub(r'\/usr.*','',output)
				output = re.sub(r'\s+',' ',output)
			result = "Compilation Error"
			return render_to_response('ccr/status.html',{'result':result,'input':inp,'output':output},context_instance=RequestContext(request))	

		#Compilation Successful
		#ipdb.set_trace()
		try:	#running
			command = "./a.out < ./codes/tmp/"+token + ".txt > ./codes/tmp/out"+token+".txt"
			os.system(command)
			f = open('./codes/tmp/out'+token+'.txt')
			output = f.read()
			f.close()
			result = "Execution Successful"
		except subprocess.CalledProcessError,er:	#error while running
			output = er.output
			result = "Execution Failed"
		
		#ipdb.set_trace()
		html = render_to_string('ccr/status.html',{'result':result,'input':inp,'output':output})
		return HttpResponse(html)
	else:
		return HttpResponseRedirect('/ccr/editor')