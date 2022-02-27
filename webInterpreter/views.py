import sys

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#create index function

@login_required(login_url='common:login')
def index(request):
    print("hi1")
    return render(request, 'webInterpreter/webInterpreter.html')

@login_required(login_url='common:login')
def runcode(request):

    print("hi2")

    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()

        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request , 'webInterpreter/webInterpreter.html', {"code":codeareadata , "output":output})
