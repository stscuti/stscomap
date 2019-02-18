from django.template import RequestContext
from django.shortcuts import render_to_response, render
from MEFCOMAP.forms import Login_Form
from django.contrib.auth import authenticate, login

def login_page(request):
    message=None
    if request.method=="POST":
        form=Login_Form(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message="Te identificaste correctamente"
                else:
                    message="Usuario inactivo"
            else:
                message="Usuario y/o Password Incorrecto"
    else:
        form=Login_Form()
    return render(request, 'login.html', {'message':message,'form':form})
    #return render_to_response('login.html', {'message':message,'form':form}, context_instance=RequestContext(request))

                    
    
