from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
	return HttpResponse('hello')
	
def whoami(request):
	sex = request.GET['sex']
	name = request.GET['name']
	response = 'You are ' + name + ' and of sex ' + sex
	return HttpResponse(response)
	
def text_form(request):
    return render(request, 'demo/text_form.html', {})
    
def post_new(request):
    form = PostForm()
    return render(request, 'demo/text_form.html', {'form': form})
