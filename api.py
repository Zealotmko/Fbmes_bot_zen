#!/usr/bin/python
# -*- coding: utf-8 -*-
#ZEN Technology 
#www.zentechnologymm.com

import json

from flask import Flask, request

__author__ = 'enginebai'

API_ROOT = 'api/'
FB_WEBHOOK = 'fb_webhook'

app = Flask(__name__)


@app.route(API_ROOT + FB_WEBHOOK, methods=["GET"])
def fb_webhook():
    verification_code = 'I_AM_VERIFICIATION_CODE'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


@app.route(API_ROOT + FB_WEBHOOK, methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        messagings = entry['messaging']
        for message in messagings:
            sender = message['sender']['id']
            if message.get('message'):
                text = message['message']['text']
                print("{} says {}".format(sender, text))
    return "Hi"


if __name__ == '__main__':
    context = ('ssl/fullchain.pem', 'ssl/privkey.pem')
    app.run(host='0.0.0.0', debug=True, ssl_context=context)
