import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from dotenv import load_dotenv
load_dotenv() 
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' + GEMINI_API_KEY

@csrf_exempt
@require_POST
def gemini_chat(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '')
        if not user_message:
            return JsonResponse({'reply': 'Please enter a message.'})
        payload = {
            "contents": [{"parts": [{"text": user_message}]}]
        }
        resp = requests.post(GEMINI_API_URL, json=payload, timeout=15)
        if resp.status_code == 200:
            result = resp.json()
            reply = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'Sorry, no response.')
            return JsonResponse({'reply': reply})
        else:
            return JsonResponse({'reply': 'Sorry, Gemini API error.'})
    except Exception as e:
        return JsonResponse({'reply': 'Error: ' + str(e)})
