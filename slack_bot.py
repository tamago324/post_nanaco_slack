#!/usr/bin/env python

import requests
import json
import os

class SlackBot():
    def __init__(self, username, iconUrl=None):
        '''
        Constractor
        :param str username:    Bot name
        :param str iconUrl: icon web url
        ex1) slackBot = SlackBot('slackbot', iconUrl='https://example/dog.jpg')

        -- free icon web site --
        http://jp.freepik.com/free-icons/animals
        '''
        self._username = username
        self._iconUrl = iconUrl

    def post_nanaco_status(self, nanaco):
        ''' Post message
        :param str message:
        '''
        payload = self.create_payload(nanaco)
        requests.post(os.environ['WEBHOOK_URL'], data=json.dumps(payload))

    def create_payload(self, nanaco):
        ''' Create payload for Nanaco object
        :param Nanaco nanaco: nanaco object
        :return: posted message payload
        '''

        payload = {'username': self._username,
                   'icon_url': self._iconUrl}

        if nanaco is None:
            payload['text'] = 'nanacoの情報が正しく取得できませんでした'
        else:
            payload['text'] = f'{nanaco.money}円/{nanaco.point}P\n{nanaco.time}'

        return payload
