from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})  # adding request object to the object
   return render_to_response('dockermon/home.html',
                             context_instance=context)
