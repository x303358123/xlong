# conding = urf-8
# from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(requset):
	# now = datetime.datetime.now()

	# html = "<html><body>It is now %s.</body></html>" % now

	# return HttpResponse(html)
	return render(requset,'index.html')



