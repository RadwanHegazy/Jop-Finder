from django.shortcuts import render
from . import scrapper



def home (request) :
    return render(request,'index.html')


def jops (request) : 

    context = {}

    if request.method == "POST" :
        keyword = request.POST['keyword']

        jops = scrapper.GetJops( keyword = keyword )

        context['jops'] = jops.jops
        context['count'] = len(jops.jops)

    return render(request,'jops.html',context)