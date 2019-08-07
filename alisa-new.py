from flask import Flask,  request
import os
from db import *


app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    response = {
            'version':request.json['version'],
            'session':request.json['session'],
            'response':{
              'text':  'Ok i show are you',
              'end_session': False
            }
    }
                
    user_id = request.json['session']['user_id']
    state = get_state(user_id)
    
    if state == 0:
        response['responce']['text'] = 'Enter you`r name '
        set_state(user_id, 1)
    elif state == 1:
        set_name(user_id, request.json['request']['original_utterance'])
        response['responce']['text'] = 'Enter you`r phone'
        set_state(user_id, 2)
    elif state == 2:
        set_phone(user_id, request.json['request']['original_utterance'])
        response['responce']['text'] = 'Enter you`r surname'
        set_state(user_id, 3)  
    elif state == 3:
        set_surname(user_id, request.json['request']['original_utterance'])
        response['responce']['text'] = 'Спасибо ваш аккаунт успешно создан'
        set_state(user_id, 4) 
    elif state == 4:
        name = getname(user_id)
        surname = get_surname(user_id)
        text = f'You name:{name}\n'
        text = text + f'You surename:{surname}\n'
        return response

app.run(host='0.0.0.0', port=os.getenv('PORT',5000))
