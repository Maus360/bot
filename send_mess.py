#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '91af6c62ef9141938f44c391a6173718'


def send_to_ai(message):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'ru'  # optional, default value equal 'en'
    request.session_id = "1eca3c13-9b01-467f-b8d4-532a995447fe"
    request.query = str(message)#"привет"
    response = request.getresponse()
    #print(response.read())
    string = response.read().decode('utf-8')
    js = json.loads(string)
    print(js)
    return js
    #print(js['result']['fulfillment']['speech'])

'''if __name__ == '__main__':
    main()
'''