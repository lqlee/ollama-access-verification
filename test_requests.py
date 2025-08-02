
import requests
import json

url = 'http://localhost:11434/api/chat'
question = 'where is the capital of USA?'
model = 'gemma3:1b' # ollama list
payload = { 'model': model, 'messages': [{'role':'user', 'content': question}] }

response = requests.post(url, json = payload, stream = True)

if response.status_code == 200 :
  print('Streaming response from Ollama : ')
  for line in response.iter_lines(decode_unicode=True) :
    if line :
      try :
        json_data = json.loads(line)
        if 'message' in json_data and 'content' in json_data['message'] :
          print(json_data['message']['content'], end='')
      except json.JSONDecodeError :
        print(f'\nFailed to parse line : {line}')
  print()


