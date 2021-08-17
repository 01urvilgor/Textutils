from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')


    if removepunc == "on":
        Punctuations = ''' ! ()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_Text' : analyzed}
        djtext = analyzed
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase', 'analyzed_Text' : analyzed}
        djtext = analyzed

    if(newlineremover=="on"): 
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed Newlines', 'analyzed_Text' : analyzed}
        djtext = analyzed
    
    if(charcounter=="on"):
        analyzed = ""
        analyzed = analyzed + str(len(djtext.replace(" ", ""))) 

        params = {'purpose': 'Number of character', 'analyzed_Text' : analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"): 
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Space', 'analyzed_Text' : analyzed}
        djtext = analyzed

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcounter != "on"):
        return HttpResponse("Enter The Operation First")
    
    return render(request, 'analyze.html', params)   