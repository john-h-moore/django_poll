#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Poll

def index(request):
	latest_poll_list = Polls.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
			'latest_poll_list': latest_poll_list,
		})
	#return HttpResponse("Hello, world. You're at the poll index.")
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." %poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." %poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." %poll_id)