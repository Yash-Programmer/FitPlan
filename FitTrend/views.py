from django.shortcuts import render
from .models import Padlet
import google.generativeai as ai


# Create your views here.
def padlet(request):
    items = Padlet.objects.order_by('name')

    context = {
        'items': items
    }

    return render(request, 'padlet.html', context)

def submit(request):
    name = request.GET.get('noteName')
    title = request.GET.get('noteTitle')
    description = request.GET.get('noteContent')
    print(name, title, description)
    padlet_ins = Padlet.objects.create(name=name, title=title, description=description)
    padlet_ins.save()
        
    return render(request, 'submit.html')

def chatbot(request):
    print(request.method)
    if request.method == "POST":
        question = request.POST.get('question')
        print(question)
        API_KEY = "AIzaSyC71aIp7u9YeRa67G1ORzgPYXtJXDnRwqY"
        ai.configure(api_key=API_KEY)
        model = ai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        answer_chat = chat.send_message(question)
        answer = answer_chat.text
        print(answer)
        context = {
            'answer': answer,
            'question': question,
        }

        return render(request, 'chatbot.html', context=context)
    else: 
        return render(request, 'chatbot.html')