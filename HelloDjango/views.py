from django.template import Template 
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context
import random
def hello(request):
    return HttpResponse("Hello world")

def testTemplate(request):
    print 'server start !'
    t = get_template('qw.html')
    randomChoice = random.choice((0,1))
    print '----',randomChoice
    return HttpResponse( t.render(Context({'randomChoice': randomChoice})))