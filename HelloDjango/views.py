from django.template import Template 
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context, RequestContext
import random
def hello(request):
    return HttpResponse("Hello world")

def testTemplate(request):
    print 'server start !'
    t = get_template('qw.html')
    randomChoice = random.choice((0,1))
    print '----',randomChoice
    return HttpResponse( t.render(Context({'randomChoice': randomChoice})))

def testMeta(request):
    t = get_template('qw.html')
    return HttpResponse(t.render(Context({'metaList': request.META.items()})))
    


def getCard(request):
    t = get_template('testForm.html')
    return HttpResponse(t.render(RequestContext(request)))

def cardList(request):
#     return HttpResponse('test')
    t = get_template('cardList.html')
    postItems = request.POST().items()
    return HttpResponse(t.render(RequestContext({'length':True})))

#     return HttpResponse(t.render(RequestContext({'postItems': postItems,'length':postItems.length})))


      