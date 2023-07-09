from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import openai
openai.api_key = settings.OPENAI_API_KEY
# print('from views ===>', settings.OPENAI_API_KEY)
# generate text 
def home(request):
    template_name = 'home.html'
    result = ''
    user_input=''
    if request.method == "POST":
        user_input = request.POST.get('userinput')
        result = generate_text(user_input)
        print('====>', user_input)
    context = {
        'result': result,
        'user_input':user_input,
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

