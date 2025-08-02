
import ollama

#client = ollama.Client(host='http://your_ollama_server_ip:11434')
client = ollama.Client()
model = 'gemma3:1b' # ollama list
prompt = 'where is the capital of USA?'

response = client.generate(model = model, prompt = prompt)
print ('Response from Ollama : ')
print (response.response)
'''
response = client.chat(
  model="llama2",
  messages=[
    {"role": "user", "content": "Tell me a fun fact about space."}
  ]
)
print(response["message"]["content"])
'''
