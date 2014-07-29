from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.producto.models import producto
from apps.producto.forms import productoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/personal/login')
def view_add(request):
	if request.method == "POST":
		form = productoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/productos")
		else:
			form  = productoForm()
			msg="Revisa bien los datos"
			ctx = {'form':form,'msg':msg}
			return render_to_response('producto/add.html',ctx,
				context_instance=RequestContext(request))
				
	else:
		form = productoForm()
		msg="Ingresa los datos"
		ctx = {'form':form,'msg':msg}
		return render_to_response('producto/add.html',ctx,
				context_instance=RequestContext(request))




@login_required(login_url='/personal/login')
def view_edit(request,id):
	p = producto.objects.get(pk=id)
	if request.method == "POST":
		form = productoForm(request.POST,instance=p)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/productos/")
		else:
			form = productoForm(p)
			msg="Revisa bien los datos"
			ctx = {'form':form,'msg':msg}
			return render_to_response('producto/edit.html',ctx,
				context_instance=RequestContext(request))
				
	else:
		form = productoForm(instance=p)
		msg="Ingresa los datos"
		ctx = {'form':form,'msg':msg}
		return render_to_response('producto/edit.html',ctx,
				context_instance=RequestContext(request))


@login_required(login_url='/personal/login')
def view_del(request,id):
	p = producto.objects.get(pk=id)
	p.delete()
	return HttpResponseRedirect("/productos/")






@login_required(login_url='/personal/login')
def view_lista(request):
    contact_list = producto.objects.all()
    paginator = Paginator(contact_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        productos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        productos = paginator.page(paginator.num_pages)

    return render_to_response('producto/lista.html', {"lista": productos},
				context_instance=RequestContext(request))



