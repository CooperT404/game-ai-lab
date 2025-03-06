from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add your code below
sign_your_name = 'Cooper Thomas'
model = 'llama3.2' # Model specified in the demo_agent.py
options = {'temperature': 0.5, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 'You should have emotions like a human being and be able to convey those emotions in your responses.'}
]

options |= {'seed': seed(sign_your_name)}

# Chat loop
while True:
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response["message"]["content"]}')
  messages.append({'role': 'assistant', 'content': response['message']['content']})
  
  if message['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string += '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)


