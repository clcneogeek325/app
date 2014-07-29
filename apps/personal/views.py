from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import (AuthenticationForm,UserCreationForm,
					UserChangeForm,PasswordChangeForm)
from django.contrib.auth import authenticate, login,logout
from apps.personal.forms import formPerfil,formUser,formEditUser
from django.contrib.auth.models import User
from apps.personal.models import Perfil
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.mail import mail_admins



		

@login_required(login_url='/personal/login')
def view_edit_passwd(request,id):
	u = User.objects.get(id=id)
	if request.method == "POST":
		form = PasswordChangeForm(u,request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		else:
			form = PasswordChangeForm(u)
			msg="Revisa bien los datos"
			ctx = {'form':form,'msg':msg}
			return render_to_response('personal/passwd.html',ctx,
				context_instance=RequestContext(request))
				
	else:
		form = PasswordChangeForm(u)
		msg="Ingresa los datos"
		ctx = {'form':form,'msg':msg}
		return render_to_response('personal/passwd.html',ctx,
				context_instance=RequestContext(request))


def view_jcalendar(request):
	return render_to_response('jcalendar.html',
		context_instance=RequestContext(request))

		
@login_required(login_url='/personal/login')
def view_edit_user(request,id):
	u = User.objects.get(id=id)
	p = Perfil.objects.get(user_id=id)
	if request.method == "POST":
		formuser = formEditUser(request.POST,instance=u)
		formperfil = formPerfil(request.POST,instance=p)
		if formuser.is_valid() and formperfil.is_valid():
			formuser.save()
			formperfil.save()
			return HttpResponseRedirect("/")
		else:
			formuser = formEditUser(request.POST)
			formperfil = formPerfil(request.POST)
			msg="Revisa bien los datos"
			ctx = {'formuser':formuser,'formperfil':formperfil,'msg':msg}
			return render_to_response('personal/edit.html',ctx,
				context_instance=RequestContext(request))
			
	else:
		formperfil= formPerfil(instance=p)
		formuser = formEditUser(instance=u)
		msg="Ingresa los datos"
		ctx = {'formuser':formuser,'formperfil':formperfil,'msg':msg}
		return render_to_response('personal/edit.html',ctx,
			context_instance=RequestContext(request))
	
				


@login_required(login_url='/personal/login')
def view_index(request):
	lsrUser = User.objects.filter(is_staff=True)
	ctx = {'lista':lsrUser}
	return render_to_response('personal/index.html',ctx,
		context_instance=RequestContext(request))

def view_login(request):
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = auth.authenticate(username=username, password=password)
	    if user is not None and user.is_active:
	        auth.login(request, user)
	        return HttpResponseRedirect("/")
	    else:
	        return HttpResponseRedirect("/personal/login")
	else:
		form = AuthenticationForm()
		ctx = {'form':form}
		return render_to_response('login.html',
			ctx,context_instance=RequestContext(request))
			
def view_logout(request):
	logout(request)
	return HttpResponseRedirect("/personal/login")



@login_required(login_url='/personal/login')
def view_del_user(request,id):
	if request.method == "POST":
		u = User.objects.get(pk=id)
		u.delete()
		return HttpResponseRedirect("/")
	else:
		msg="Estas seguro de querelo eliminar"
		ctx = {'msg':msg}
		return render_to_response('personal/confirm.html',ctx,
			context_instance=RequestContext(request))
		


@login_required(login_url='/personal/login')
def view_add_user(request):
	if request.method == "POST":
		formuser = UserCreationForm(request.POST)
		formdatos = formUser(request.POST)
		formperfil = formPerfil(request.POST)
		if formuser.is_valid() and formperfil.is_valid() and formdatos.is_valid():
			u = formuser.save()
			user = User.objects.get(pk=u.id)
			nombres   = request.POST['first_name']
			apellidos = request.POST['last_name']
			email     = request.POST['email']
			drecc     = request.POST['direccion']
			telef     = request.POST['telefono']
			user.last_name   = apellidos
			user.first_name  = nombres
			user.email       = email
			user.is_staff    = True
			user.is_active   = True
			user.is_superuser = False
			user.save()
			p = Perfil(user_id=u.id,direccion=drecc,telefono=telef)
			p.save()
			return HttpResponseRedirect("/")
		else:
			msg = "Revise bien los datos por fabor"
			return get_add(request,msg)
	else:
		msg = "Llene la informacion que se pide"
		return get_add(request,msg)


def get_add(request,msg):
	formuser = UserCreationForm()
	formdatos = formUser()
	formperfil = formPerfil()
	ctx = {'formuser':formuser,
		'formdatos':formdatos,
		'formperfil':formperfil,
		"msg":msg}
	return render_to_response('personal/add.html',
			ctx,context_instance=RequestContext(request))







