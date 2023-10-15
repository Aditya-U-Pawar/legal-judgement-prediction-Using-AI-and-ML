from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import JsonResponse
import openai

# Create your views here.
#password adicto$$$***000

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    reponse = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop=None,
        temperature=0.7,
    )
    print(reponse)
    answer = reponse.choices[0].text.strip()
    return answer

def chatterbot(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatterbot.html')


#def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is homepage")



def Law4People(request):
    
    template = loader.get_template('Law4People.html')
    return HttpResponse(template.render())

def logout(request):
    template = loader.get_template('logout.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

