#Self-made

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    analyzed = request.POST.get("text")
    task = request.POST.get("flexRadioDefault")
    parameters = {'Result':"Analyzed text",'analyzed_text':analyzed}
    if analyzed == "":
        return HttpResponse('<script>alert("Please provide some text");window.location="/"</script>')
    else:      
        if task == "countchar":
            count = 0
            for char in analyzed:
                if not char == " ":
                    count+=1
            analyzed=count
            parameters = {'Result':'Count of characters','analyzed_text':analyzed}
            return render(request, 'analyze.html', parameters)
        elif task == "newlineremover":
            newstring=""
            for char in analyzed:
                if char!="\n" and char!="\r":
                    newstring = newstring + char

            parameters = {'Result':"Analyzed text - New line removed",'analyzed_text':newstring}
            print(newstring)
            return render(request, 'analyze.html', parameters)
        elif task == "removepunc":
            pun = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
            newstring = ""
            for char in analyzed:
                if char not in pun:
                    newstring = newstring + char
            parameters = {'Result':"Analyzed text - Punctuations removed",'analyzed_text':newstring}
            return render(request, 'analyze.html', parameters)
        elif task == "changeupper":
            newstring = ""
            for char in analyzed:
                newstring = newstring + char.upper()
            parameters = {'Result':"Analyzed text - Changed to Uppercase",'analyzed_text':newstring}
            return render(request, 'analyze.html', parameters)
        else:
            return HttpResponse('<script>alert("Please select any of the option");window.location="/"</script>')