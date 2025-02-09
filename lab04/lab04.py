from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import TemplateChat

def run_console_chat(sign, **kwargs):
    chat = TemplateChat.from_file(sign=sign, **kwargs)
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        try:
            message = chat_generator.send(input('You: '))
            print('Agent:', message)
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

lab04_params = {
    'template_file': r'C:\Users\labadmin\Desktop\spring2025-labs\lab04\lab04_trader_chat.json',
    'sign': 'Cooper',
    'end_regex': r'End of trade'  # Adjust according to your template's end condition
}



if __name__ == '__main__':
    sign = lab04_params['sign']
    template_file = lab04_params['template_file']
    end_regex = lab04_params['end_regex']
    
    run_console_chat(sign=sign, template_file=template_file, end_regex=end_regex)
