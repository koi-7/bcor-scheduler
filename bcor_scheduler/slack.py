# coding: utf-8


import requests


class Slack:
    def __init__(self, channel_id, token):
        self.__channel_id = channel_id
        self.__token = token

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def token(self):
        return self.__token

    def notify(self, text):
        api_url = 'https://slack.com/api/chat.postMessage'
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'channel': self.channel_id, 'text': text}
        requests.post(api_url, headers=headers, data=data)
