from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import openai
openai.api_key = settings.OPENAI_API_KEY

# generate text 
def home(request):
    template_name = 'home.html'
    result = ''
    if request.method == "POST":
        user_input = request.POST.get('animal')
        result = generate_text(user_input)
    context = {
        'result': result,
    }
    return render(request, template_name, context)


def generate_text(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

